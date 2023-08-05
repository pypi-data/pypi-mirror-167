from typing import List
import numpy as np
from pydantic import BaseModel


class NodeInfo(BaseModel):
    node_name:str
    parent:str
    level_ai:int
    description:str
    
    
def dict_swap_key_and_values(dicti):
    all_values = list(dicti.values())
    assert np.unique(all_values).shape[0] == len(all_values), "values sind nicht alle unique"
    dicti_swap = dict([(b, a) for a, b in dicti.items()])
    return dicti_swap

    

class SectionMapping():
    dict_level_ai_to_level_name = {1:"abschnitt",2:"kapitel",3:"positionen",4:"hs",5:"kn", 6:"taric", 7:"ezt"}  
    dict_level_name_to_level_ai = dict_swap_key_and_values(dict_level_ai_to_level_name)

    
    dict_node_name_len_to_level_ai = {3:1,
                                      2:2,
                                      4:3,
                                      6:4,
                                      8:5}
    dict_level_ai_to_node_name_len = dict_swap_key_and_values(dict_node_name_len_to_level_ai)


    dict_abschnitt_idx_to_num_kapitel_range = {
        "A01": list(range(1,6)),
        "A02": list(range(6,15)),
        "A03": list(range(15,16)),
        "A04": list(range(16,25)),
        "A05": list(range(25,28)),
        "A06": list(range(28,39)),
        "A07": list(range(39,41)),
        "A08": list(range(41,44)),
        "A09": list(range(44,47)),
        "A10": list(range(47,50)),
        "A11": list(range(50,64)),
        "A12": list(range(64,68)),
        "A13": list(range(68,71)),
        "A14": list(range(71,72)),
        "A15": list(range(72,77))+list(range(78,84)),
        "A16": list(range(84,86)),
        "A17": list(range(86,90)),
        "A18": list(range(90,93)),
        "A19": list(range(93,94)),
        "A20": list(range(94,97)),
        "A21": list(range(97,100)),
            }


    for key in dict_abschnitt_idx_to_num_kapitel_range:
        range_v = [str(i) for i in dict_abschnitt_idx_to_num_kapitel_range[key]]
        dict_abschnitt_idx_to_num_kapitel_range[key]  = ["0"+i if len(i)==1 else i for i in range_v]

    dict_kapitel_to_abschnitt = {}
    for ti in dict_abschnitt_idx_to_num_kapitel_range:
        for to in dict_abschnitt_idx_to_num_kapitel_range[ti]:
            to = str(to)
            dict_kapitel_to_abschnitt[to] = ti




class WNKTraversal():
    """
    Traversal through tree object
    - useable for wnk_tree_ai and wnk_tree_view
    """
    def _just_identifier(nodes) -> List[str]:
        return [i.identifier for i in nodes]

    def get_path_to_node(wnk_tree, node_akt:str) -> List[str]:
        """ '46' -> ['A09', '46']"""
        path_to_node_v = [node_akt]
        while node_akt !="root":
            node_akt = wnk_tree.tree.parent(node_akt).identifier
            path_to_node_v.append(node_akt)
        path_to_node_v = path_to_node_v[::-1][1:] # ohne root
        return path_to_node_v

    def get_children_of_node(wnk_tree:object, node_name:str) -> List[str]:
        children_nodes = wnk_tree.tree.children(node_name)
        children_nodes = WNKTraversal._just_identifier(children_nodes)
        content = sorted(children_nodes)
        return content

    def get_siblings_of_node(wnk_tree:object, node_name:str, add_self:bool=True) -> list:
        siblings_nodes = wnk_tree.tree.siblings(node_name)
        if add_self:
            self_node = wnk_tree.tree.get_node(node_name)
            siblings_nodes.append(self_node)
        siblings_nodes = WNKTraversal._just_identifier(siblings_nodes)
        content = sorted(siblings_nodes)
        return content

    def get_parent_node(wnk_tree:object, node_name:str) -> str:
        if node_name == "root":
            return None
        parent_node = wnk_tree.tree.parent(node_name).identifier
        return parent_node


class WNKTraversalAINodeData():
    """
    just wnk traversal without ai inference
    - only for wnk_tree_ai
    """

    def get_children_data_of_node(wnk_tree_ai:object, node_name:str) -> List[NodeInfo]:
        children_nodes = wnk_tree_ai.tree.children(node_name)

        children_nodes = [NodeInfo(  node_name = node.identifier,
                                        description = node.data["acc_description"][-1],
                                        level_ai = node.data["level_ai"],
                                        parent = node.data["parent"]).dict()
                            for node in children_nodes]

        content = sorted(children_nodes, key = lambda k:k["node_name"])
        return content

    def get_data_of_node(wnk_tree_ai:object, node_name:str) -> NodeInfo:
        node = wnk_tree_ai.tree.get_node(node_name)
        node_data = NodeInfo(node_name = node.identifier,
                                description = node.data["acc_description"][-1],
                                level_ai = node.data["level_ai"],
                                parent = node.data["parent"]).dict()
        return node_data

    def get_path_data_of_node(wnk_tree_ai:object, node_name:str) -> List[NodeInfo]:
        node_name_path_v = WNKTraversal.get_path_to_node(wnk_tree_ai, node_name)
        content = []
        for node_name_in_path in node_name_path_v:
            node = wnk_tree_ai.tree.get_node(node_name_in_path)
            node_data = NodeInfo(node_name = node.identifier,
                                    description = node.data["acc_description"][-1],
                                    level_ai = node.data["level_ai"],
                                    parent = node.data["parent"]).dict()
            content.append(node_data)
        return content











