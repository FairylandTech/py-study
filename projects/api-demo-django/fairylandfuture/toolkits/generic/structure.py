# coding: UTF-8
"""
@software: PyCharm
@author: Lionel Johnson
@contact: https://fairy.host
@organization: https://github.com/FairylandFuture
@datetime: 2024-12-23 16:35:23 UTC+08:00
"""

from typing import Dict, Any, List, Optional, Sequence, Tuple

from fairylandfuture.core.superclass.structures import BaseStructureTreeNode


class TreeBuilder:
    node = BaseStructureTreeNode

    @classmethod
    def build(cls, data: Sequence[Dict[str, Any]], id_field: str = "id", parent_id_field: str = "parent_id") -> Tuple[Dict[str, Any], ...]:
        if not data:
            raise ValueError("Input data cannot be empty.")

        nodes = {item.get(id_field): cls.node(item.get(id_field), parent_id=item.get(parent_id_field), data=item) for item in data}
        root_nodes = []

        for node in nodes.values():
            parent_id = node.parent_id
            if parent_id and parent_id in nodes:
                nodes[parent_id].add_child(node)
            else:
                root_nodes.append(node)

        return tuple([node.to_dict() for node in root_nodes])


class TreeBuilderV2(TreeBuilder):

    @classmethod
    def build(
            cls,
            data: Sequence[Dict[str, Any]],
            id_field: str = "id",
            parent_id_field: str = "parent_id",
            max_depth: Optional[int] = None
    ) -> Tuple[Dict[str, Any], ...]:

        if not data:
            raise ValueError("Input data cannot be empty.")

        nodes = {
            item.get(id_field): cls.node(item.get(id_field), parent_id=item.get(parent_id_field), data=item)
            for item in data
        }
        root_nodes = []

        for node in nodes.values():
            parent_id = node.parent_id
            if parent_id and parent_id in nodes:
                nodes[parent_id].add_child(node)
            else:
                root_nodes.append(node)

        return tuple([cls.__limit_depth(node.to_dict(), max_depth) for node in root_nodes])

    @classmethod
    def __limit_depth(cls, node: Dict[str, Any], max_depth: Optional[int], current_depth: int = 1) -> Dict[str, Any]:
        if max_depth is not None and current_depth >= max_depth:
            node.pop("children", None)
        else:
            children = node.get("children", [])
            node["children"] = [
                cls.__limit_depth(child, max_depth, current_depth + 1)
                for child in children
            ]
        return node
