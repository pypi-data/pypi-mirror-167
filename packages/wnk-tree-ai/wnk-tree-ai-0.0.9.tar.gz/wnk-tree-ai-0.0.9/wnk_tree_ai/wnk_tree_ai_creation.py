import pandas as pd
from treelib import Tree, Node
from typing import List, Tuple, Dict, Optional, Union
from enum import Enum
import pydantic
from pydantic import BaseModel

from wnk_tree_ai.wnk_tree_ai_utils import WNKTraversal

def type_save(type_model:pydantic, data:Union[List[dict],dict]):
    """ ensure type save data """
    if type(data)==dict:
        data = type_model(**data).dict()
    elif type(data)==list:
        type_model_inner = type_model.__reduce__()[1][1]
        data = [type_model_inner(**item).dict() for item in data]
    else: 
        assert False
    return data


class WNKAINodeType(Enum):
    """ 
        root-|intermediate-|endline- node 
    +++ normal-|padding- node 
    +++ 
    """
    ROOT_NODE:str = "ROOT_NODE" # black
    INTERMEDIATE_PADDING_NODE_BRANCH:str = "INTERMEDIATE_PADDING_NODE_BRANCH" # blue
    INTERMEDIATE_PADDING_NODE_NON_BRANCH:str = "INTERMEDIATE_PADDING_NODE_NON_BRANCH" # orange
    INTERMEDIATE_NODE_BRANCH:str = "INTERMEDIATE_NODE_BRANCH" # green
    INTERMEDIATE_NODE_NON_BRANCH:str = "INTERMEDIATE_NODE_NON_BRANCH" # grey
    ENDLINE_PADDING_NODE_SIBLINGS:str = "ENDLINE_PADDING_NODE_SIBLINGS" # yellow
    ENDLINE_PADDING_NODE_NON_SIBLINGS:str = "ENDLINE_PADDING_NODE_NON_SIBLINGS" # red
    
class WNKAINodeTypeAttr(BaseModel):
    is_root:bool
    is_endline:bool
    is_one_to_one_relation:bool # one parent (as always, besides root node), but just one children
    has_siblings:bool

class WNKTreeAIData(BaseModel):
    node_name:str
    parent:str
    level_ai:int
    beschreibung:str
    keywords_f:List[str]
    

class WNKAINodeTypeAnlysis:
    """ """
    @classmethod
    def is_root(cls, tree, node) -> bool:
        return node.is_root()

    @classmethod
    def is_endline(cls, tree, node) -> bool:
        return node.is_leaf()
    
    @classmethod
    def is_one_to_one_relation(cls, tree, node) -> bool:
        value = len(tree.children(node.identifier))==1
        return value
    
    @classmethod
    def has_siblings(cls, tree, node) -> bool:
        value = len(tree.siblings(node.identifier))>0
        return value
    
    @classmethod
    def _is_true(cls, attr:dict, keys_true_v:List[str], keys_v:List[str]):
        keys_false_v = [key for key in keys_v if key not in keys_true_v]
        is_ok = True
        for key in keys_true_v: 
            if not attr[key]: is_ok=False
        for key in keys_false_v:
            if attr[key]: is_ok=False
        return is_ok
        
    @classmethod
    def get_type_code(cls, attr:dict) -> str:
        keys_v = ['is_root', 'is_endline', 'is_one_to_one_relation', 'has_siblings']
        if cls._is_true(attr, ["is_root"], keys_v):
            return WNKAINodeType.ROOT_NODE.name
        if cls._is_true(attr, [], keys_v):
            return WNKAINodeType.INTERMEDIATE_PADDING_NODE_BRANCH.name
        if cls._is_true(attr, ["is_one_to_one_relation"], keys_v):
            return WNKAINodeType.INTERMEDIATE_PADDING_NODE_NON_BRANCH.name
        if cls._is_true(attr, ["is_one_to_one_relation","has_siblings"], keys_v):
            return WNKAINodeType.INTERMEDIATE_NODE_NON_BRANCH.name
        if cls._is_true(attr, ["has_siblings"], keys_v):
            return WNKAINodeType.INTERMEDIATE_NODE_BRANCH.name
        if cls._is_true(attr, ["is_endline"], keys_v):
            return WNKAINodeType.ENDLINE_PADDING_NODE_NON_SIBLINGS.name
        if cls._is_true(attr, ["is_endline","has_siblings"], keys_v):
            return WNKAINodeType.ENDLINE_PADDING_NODE_SIBLINGS.name
        assert False, "muss einen matchen!"
    
    @classmethod
    def get_node_type_attr(cls, tree, node:Node) -> dict:
        node_type_attr = WNKAINodeTypeAttr(is_root=cls.is_root(tree,node),
                                              is_endline=cls.is_endline(tree,node),
                                              is_one_to_one_relation=cls.is_one_to_one_relation(tree,node),
                                              has_siblings=cls.has_siblings(tree,node))
        node_type_attr = node_type_attr.dict()
        return node_type_attr



    
class WNK():
    """
    Beinhaltet die Warennomenklatur für die ai-tree-structure (5-level Modell)
    """
    def __init__(self, path_to_wnk_file:str = None, wnk_tree_ai_data_v:List[WNKTreeAIData] = None):
        assert any([path_to_wnk_file, wnk_tree_ai_data_v])
        
        if path_to_wnk_file is not None:
            wnk_tree_ai_data_v = self._load_and_prepare_from_df(path_to_wnk_file)
        wnk_tree_ai_data_v = type_save(List[WNKTreeAIData], wnk_tree_ai_data_v)
        
        self.tree = self._create_tree(wnk_tree_ai_data_v)
        self._add_post_init_info()
        
    def _load_and_prepare_from_df(self, path_to_file:str): ### !!! naming von column in csv anpassen
        """ läd und prepariert einen df (csv file) immer in der gleichen weise """
        column_names = WNKTreeAIData.schema()["properties"].keys()
        df = pd.read_csv(path_to_file, dtype=str).fillna("None")
        wnk_tree_ai_data_v = df[column_names].to_dict("records")
        for item in wnk_tree_ai_data_v:
            for column in item:
                update = None
                try:
                    temp = eval(item[column])
                    if type(temp)==list: update = temp
                    else: update = item[column]
                except: pass
                else: item[column] = update
        return wnk_tree_ai_data_v

    def _create_tree(self, wnk_tree_ai_data_v:List[dict]):
        
        tree = Tree()
        root_data = {"description":"root",  "keywords":[], "level_ai":0, "parent":"root"}
        tree.create_node("root", "root", data = root_data)  # No parent means its the root node

        for item in wnk_tree_ai_data_v:
            parent = item["parent"]
            node_name = item["node_name"]
            level_ai = item["level_ai"]
            description = item["beschreibung"]
            keywords = item["keywords_f"]

            data = {"description": description,
                    "keywords": keywords,
                    "level_ai":level_ai,
                    "parent": parent}
            tree.create_node(node_name,  node_name, parent=parent, data=data)
        return tree

    def _add_post_init_info(self):
        ### add node type infos
        for node in self.tree.all_nodes():
            node_type_attr = WNKAINodeTypeAnlysis.get_node_type_attr(self.tree, node)
            node_type_code = WNKAINodeTypeAnlysis.get_type_code(node_type_attr)
            node.data["node_type_attr"] = node_type_attr
            node.data["node_type_code"] = node_type_code
            
        ## add acc data
        for node in self.tree.all_nodes():
            path_to_node_v = WNKTraversal.get_path_to_node(self, node.identifier)
            node.data["acc_keywords"] = [self.tree.get_node(identifier).data["keywords"] for identifier in path_to_node_v]
            node.data["acc_description"] = [self.tree.get_node(identifier).data["description"] for identifier in path_to_node_v]

        ### 
        dict_level_ai_to_node_names = {}
        for i in self.tree.all_nodes():
            if i.data["level_ai"] not in dict_level_ai_to_node_names: dict_level_ai_to_node_names[i.data["level_ai"]] = []
            dict_level_ai_to_node_names[i.data["level_ai"]].append(i.identifier)
        self.dict_level_ai_to_node_names = dict_level_ai_to_node_names













    