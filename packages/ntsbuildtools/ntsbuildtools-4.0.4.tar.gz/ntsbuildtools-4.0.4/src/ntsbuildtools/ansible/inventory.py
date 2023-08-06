from configparser import ConfigParser, NoSectionError
from dataclasses import dataclass, field
from functools import reduce
from typing import Set


def flatten(lst):
    return [item for sublist in lst for item in sublist]


@dataclass
class InventoryNode:
    """Represents a host or group of hosts.

    Has a name and parent/children relationships.
    """
    name: str
    children: Set = field(default_factory=set)
    parents: Set = field(default_factory=set)

    def __hash__(self):
        return hash(self.name)

    def add_child(self, child):
        """Add a child to this nodes children."""
        self.children.add(child)

    def add_parent(self, parent):
        """Add a parent to this nodes parents."""
        self.parents.add(parent)

    def get_ancestors(self) -> Set['InventoryNode']:
        """Return the set of ancestors of this node.
        """
        if self.parents:
            ancestors = reduce(Set.union, map(InventoryNode.get_ancestors, self.parents))
            return self.parents.union(ancestors)
        else:
            return set()

    def __str__(self):
        return self.name

    def __repr__(self):
        """Creates a useful representation for debugging.

        Returns:
            str: This object with parents and children listed as strings.
        """
        children_names = [child.name for child in self.children]
        parent_names = [parent.name for parent in self.parents]
        return f'InventoryNode(name={self.name}, children=set({children_names}), parents=set({parent_names}))'


def strip_ansible_group_name_metadata(group_name):
    return group_name.replace(':children', '') 


class InventoryTree:
    def __init__(self, path: str):
        """Ansible Inventory.

        Enables traversing and querying an Ansible Inventory (e.g. your ini-style "hosts" file).

        Args:
            path (str): Path to the Ansible Inventory config file, your ini-style `hosts` file.
        """
        self.nodes = set()
        self.root = set()
        config = ConfigParser(allow_no_value=True)
        config.read(path)
        self._init_nodes(config)
        self._init_nodes_relationships(config)
        self._init_root()

    def get_node(self, name: str) -> InventoryNode:
        """Find node in this tree.

        Does not ensure the node name is unique -- will return first node with name. 
        """
        name = strip_ansible_group_name_metadata(name)
        for node in self.nodes:
            if node.name == name:
                return node
        raise LookupError(f'Unable to find node with name: {name}')

    def _init_nodes(self, config: ConfigParser):
        """Add all hosts and groups to the tree."""
        for group_name in config.sections():
            self.nodes.add(InventoryNode(strip_ansible_group_name_metadata(group_name)))
            for host_or_group_name in config.options(group_name):
                self.nodes.add(InventoryNode(host_or_group_name))

    def _init_nodes_relationships(self, config: ConfigParser):
        """Establish parent-child relationships within this tree.

        Expects all the nodes to already be initialized.
        """
        groups = [self.get_node(group_name) for group_name in config.sections()]
        for group in groups:
            try:
                group_member_names = config.options(group.name)
            except NoSectionError:
                group_member_names = config.options(f'{group.name}:children')
            for host_or_group_name in group_member_names:
                host_or_group = self.get_node(host_or_group_name)
                group.add_child(host_or_group)
                host_or_group.add_parent(group)

    def _init_root(self):
        """Establish the root set of this tree.

        TODO: Discuss what this really means.

        Expects parent-child relationships to already be established within this tree.
        """
        for node in self.nodes:
            if not node.parents:
                self.root.add(node)
