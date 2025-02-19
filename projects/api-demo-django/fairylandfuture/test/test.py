# coding: UTF-8
"""
@software: PyCharm
@author: Lionel Johnson
@contact: https://fairy.host
@organization: https://github.com/FairylandFuture
@datetime: 2024-12-24 17:33:39 UTC+08:00
"""

from dataclasses import dataclass, field

from typing import Dict, Any, List


@dataclass
class BaseStructureTreeNode:
    id: Any
    parent_id: Any
    data: Dict[str, Any]
    children: List["StructureNode"] = field(default=None)

    def __post_init__(self):
        self.children = []

    def get_id(self) -> Any:
        return self.id

    def get_parent_id(self) -> Any:
        return self.parent_id

    def add_child(self, child: "StructureNode"):
        self.children.append(child)

    def get_children(self) -> List["StructureNode"]:
        return self.children

    def to_dict(self) -> Dict:
        result = {"id": self.id, "parent_id": self.parent_id, "data": self.data, "children": [child.to_dict() for child in self.children]}
        return result


class TreeBuilder:
    node = BaseStructureTreeNode

    @classmethod
    def build(cls, data: List[Dict[str, Any]], id_field: str = None, parent_id_field: str = None) -> List[Dict[str, Any]]:
        if not data:
            raise RuntimeError("Data is empty.")
        if not id_field:
            id_field = "id"
        if not parent_id_field:
            parent_id_field = "parent_id"

        nodes = dict()
        root_nodes = list()

        for item in data:
            node_id = item.get(id_field)
            parent_id = item.get(parent_id_field)
            node_data = item.copy()

            node = cls.node(id=node_id, parent_id=parent_id, data=node_data)
            nodes.update({node_id: node})

        for node in nodes.values():
            parent_id = node.get_parent_id()
            if parent_id is None or parent_id not in nodes:
                root_nodes.append(node)
            else:
                parent = nodes.get(parent_id)
                parent.add_child(node)

        return [node.to_dict() for node in root_nodes]
