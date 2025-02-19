# coding: UTF-8
"""
@software: PyCharm
@author: Lionel Johnson
@contact: https://fairy.host
@organization: https://github.com/FairylandFuture
@datetime: 2024-12-24 17:37:12 UTC+08:00
"""


class BaseStructureTreeNode(object):
    def __init__(self, node_id, parent_id, data):
        self.id = node_id
        self.parent_id = parent_id
        self.data = data
        self.children = []

    def get_id(self):
        return self.id

    def get_parent_id(self):
        return self.parent_id

    def add_child(self, child):
        self.children.append(child)

    def get_children(self):
        return self.children

    def to_dict(self):
        return {
            "id": self.id,
            "parent_id": self.parent_id,
            "data": self.data,
            "children": [child.to_dict() for child in self.children]
        }


class TreeBuilder(object):
    node = BaseStructureTreeNode

    @classmethod
    def build(cls, data, id_field=None, parent_id_field=None):
        if not data:
            raise RuntimeError("Data is empty.")
        if not id_field:
            id_field = "id"
        if not parent_id_field:
            parent_id_field = "parent_id"

        nodes = {}
        root_nodes = []

        for item in data:
            node_id = item.get(id_field)
            parent_id = item.get(parent_id_field)
            node_data = item.copy()

            node = cls.node(node_id=node_id, parent_id=parent_id, data=node_data)
            nodes[node_id] = node

        for node in nodes.values():
            parent_id = node.get_parent_id()
            if parent_id is None or parent_id not in nodes:
                root_nodes.append(node)
            else:
                parent = nodes.get(parent_id)
                parent.add_child(node)

        return [node.to_dict() for node in root_nodes]
