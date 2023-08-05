import sys
import json
from typing import Union, IO, Sequence
from rdflib import Graph, URIRef, BNode, Literal
from codemeta.common import AttribDict, license_to_spdx, SDO, CONTEXT, CODEMETA_SOURCE, CODEMETA_LOCAL_SOURCE, SCHEMA_SOURCE, SCHEMA_LOCAL_SOURCE, STYPE_SOURCE, STYPE_LOCAL_SOURCE, IODATA_SOURCE, IODATA_LOCAL_SOURCE, init_context, REPOSTATUS_LOCAL_SOURCE, REPOSTATUS_SOURCE, get_subgraph

def flatten_singletons(data): #TODO: no longer used, remove
    """Recursively flattens singleton ``key: { "@id": uri }`` instances to ``key: uri``"""
    if isinstance(data, dict):
        for key, value in data.items():
            if isinstance(value, dict):
                if '@id' in value and len(value) == 1:
                    data[key] = value['@id']
                elif 'id' in value and len(value) == 1:
                    data[key] = value['id']
                else:
                    data[key] = flatten_singletons(data[key])
            else:
                data[key] = flatten_singletons(data[key])
        return data
    elif isinstance(data, (list,tuple)):
        return [ x['@id'] if isinstance(x, dict) and '@id' in x and len(x) == 1 else flatten_singletons(x) for x in data ]
    else:
        return data

def remove_blank_ids(data):
    """Recursively remove all blank node IDs"""
    if isinstance(data, dict):
        if '@id' in data and data['@id'].startswith("_:"):
            del data['@id']
        if 'id' in data and data['id'].startswith("_:"):
            del data['id']
        return { k: remove_blank_ids(v) for k,v in data.items() }
    elif isinstance(data, (list, tuple)):
        return [ remove_blank_ids(v) for v in data ]
    else:
        return data

def alt_sort_key(data) -> str:
    if isinstance(data, dict):
        if 'name' in data:
            return data['name']
        if '@id' in data:
            return data['@id']
        if 'identifier' in data:
            return data['identifier']
    elif isinstance(data, str):
        return data
    return "~" #just a high alphanumeric character so it ends up after normal (ascii) stuff


def sort_by_position(data):
    """If list items have a position (schema:position) index, make sure to use it for sorting. If not, sort alphabetically of name of id"""
    if isinstance(data, (list, tuple)):
        if any( isinstance(x, dict) and 'position' in x for x in data ):
            try:
                return list(sorted( ( sort_by_position(x) for x in data) , key=lambda x: x['position'] if isinstance(x, dict) and 'position' in x else 99999999 ) )
            except TypeError: #in rare cases this might fail because of some inconsistency, return unsorted then
                return [ sort_by_position(x) for x in data ]
        else:
            try:
                return list(sorted( ( sort_by_position(x) for x in data) , key=lambda x: alt_sort_key(x) ) )
            except TypeError: #in rare cases this might fail because of some inconsistency, return unsorted then
                return [ sort_by_position(x) for x in data ]
    elif isinstance(data, dict):
        for key, value in data.items():
            data[key] = sort_by_position(value)
    return data


def normalize_schema_org(g: Graph):
    #there is debate on whether to use https of http for schema.org,
    #codemeta 2.0 uses http still in their context so we force that here too
    #(https://schema.org/docs/faq.html#19)
    for s, p, o in g.triples():
        if str(s).startswith("https://schema.org"):
            g.remove((s, p, o))
            g.add((URIRef(str(s).replace("https", "http")), p, o))

        if str(p).startswith("https://schema.org"):
            g.remove((s, p, o))
            g.add((s, URIRef(str(p).replace("https", "http")), p, o))

        if str(o).startswith("https://schema.org"):
            g.remove((s, p, o))
            g.add((s, p, URIRef(str(o).replace("https", "http"))))

def cleanup(data):
    """Recursively removes namespace prefixes from dictionary keys and use @id and @type rather than the id/type aliases"""
    if isinstance(data, dict):
        if 'id' in data:
            data['@id'] = data['id']
            del data['id']
        if 'type' in data:
            data['@type'] = data['type']
            del data['type']
        return { key.replace('schema:','').replace('http://schema.org/','').replace('codemeta:','').replace('stypes:','') : cleanup(value) for key, value in data.items() }
    elif isinstance(data, (list,tuple)):
        return [ cleanup(x) for x in data ]
    else:
        return data




#rdflib doesn't do 'framing' so we have to do it in this post-processing step:
#source: Niklas Lindström, https://github.com/libris/lxltools/blob/489c66b3fef8850077f2e6b4ba009b91aa6bf79c/lddb/ld/frame.py
#c.f. https://groups.google.com/g/rdflib-dev/c/U9Czox7kQL0?pli=1
class AutoFrame:
    def __init__(self, data):
        self.context = data.get("@context")
        self.graph_key = "@graph"
        self.id_keys = ["@id",'id'] #schema/codemata map 'id' to '@id' so we check for both
        self.rev_key = "@reverse"
        self.embedded = set()
        self.itemmap = {}
        self.revmap = {}
        self.reembed = True
        self.pending_revs = []
        for item in data.get(self.graph_key, ()):
            for p, objs in item.items():
                if p in self.id_keys:
                    self.itemmap[objs] = item
                else:
                    if not isinstance(objs, list):
                        objs = [objs]
                    for o in objs:
                        if not isinstance(o, dict):
                            continue
                        target_id = self.get_id_key(o)
                        if target_id:
                            self.revmap.setdefault(target_id, {}
                                    ).setdefault(p, []).append(item)

    def get_id_key(self, data):
        if isinstance(data,dict):
            for k in self.id_keys:
                if k in data:
                    return data[k]
        return None

    def run(self, main_id):
        main_item = self.itemmap.get(main_id)
        if not main_item:
            return None
        self.embed(main_id, main_item, set(), self.reembed)
        self.add_reversed()
        if self.context:
            main_item['@context'] = self.context
        return main_item

    def embed(self, item_id, item, embed_chain, reembed):
        self.embedded.add(item_id)
        embed_chain.add(item_id)
        for p, o in item.items():
            item[p] = self.to_embedded(o, embed_chain, reembed)
        revs = self.revmap.get(item_id)
        if revs:
            self.pending_revs.append((item, embed_chain, revs))

    def add_reversed(self):
        for item, embed_chain, revs in self.pending_revs:
            for p, subjs in revs.items():
                for subj in subjs:
                    subj_id = self.get_id_key(subj)
                    if subj_id and subj_id not in embed_chain:
                        if subj_id not in self.embedded:
                            item.setdefault(self.rev_key, {}
                                    ).setdefault(p, []).append(subj)
                            self.embed(subj_id, subj, set(embed_chain), False)

    def to_embedded(self, o, embed_chain, reembed):
        if isinstance(o, list):
            return [self.to_embedded(lo, embed_chain, reembed) for lo in o]
        if isinstance(o, dict):
            o_id = self.get_id_key(o)
            if o_id and o_id not in embed_chain and (
                    reembed or o_id not in self.embedded):
                obj = self.itemmap.get(o_id)
                if obj:
                    self.embed(o_id, obj, set(embed_chain), reembed)
                    return obj
        return o

def find_main(data, res: Union[URIRef,None]):
    """Find the main item in the graph"""
    if '@graph' in data:
        for item in data:
            if isinstance(item, dict) and item.get("@id") == str(res):
                return item, data
        return None, None
    else:
        return data, None


def rewrite_context(context) -> list:
    """Rewrite local contexts to their remote counterparts"""
    if isinstance(context, list):
        for i, value in enumerate(context):
            if value == CODEMETA_LOCAL_SOURCE:
                context[i] = CODEMETA_SOURCE
            elif value == SCHEMA_LOCAL_SOURCE:
                context[i] = SCHEMA_SOURCE
            elif value == STYPE_LOCAL_SOURCE:
                context[i] = STYPE_SOURCE
            elif value == IODATA_LOCAL_SOURCE:
                context[i] = IODATA_SOURCE
            elif value == REPOSTATUS_LOCAL_SOURCE:
                context[i] = REPOSTATUS_SOURCE
    elif isinstance(context, str):
        context = rewrite_context([context])
    return context

def serialize_to_jsonld(g: Graph, res: Union[Sequence,URIRef,None]) -> dict:
    """Serializes the RDF graph to JSON, taking care of 'framing' for embedded nodes"""

    if res:
        #Get the subgraph that focusses on this specific resource (or multiple)
        if isinstance(res, (list,tuple)):
            g = get_subgraph(g, res)
        else:
            g = get_subgraph(g, [res])

    data = json.loads(g.serialize(format='json-ld', auto_compact=True, context=CONTEXT))

    #rdflib doesn't do 'framing' so we have to do it in this post-processing step
    #if we have a single resource
    if res and (not isinstance(res, (list,tuple)) or len(res) == 1):
        data = AutoFrame(data).run(str(res)) or data

        root, parent = find_main(data, res)
        if parent and len(data['@graph']) == 1 and res:
            #No need for @graph if it contains only one item now:
            parent.update(root)
            del data['@graph']
            root = parent

    data = sort_by_position(data)
    if '@context' in data:
        data['@context'] = rewrite_context(data['@context'])

    #we may have some lingering prefixes which we don't need, cleanup:
    data = cleanup(data)


    return data
