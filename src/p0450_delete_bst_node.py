"""Problem 450. Delete a node from a BST."""


class TreeNode:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None


class BinSearchTree:
    def __init__(self, root):
        self.root = root

    def delete_node(self, key):
        # Find key parent
        parent = self.find_parent(key)
        if parent is not None:
            if parent == self.root and self.root.key == key:

        # Remove node and update tree
        self.remove_child(parent, key)

    def find_parent(self, key):
        if self.root is None:
            return None
        elif self.root.key == key:
            return self.root
        node = self.root
        while node:
            if (
                (node.left and node.left.key == key)
                or (node.right and node.right.key == key)
            ):
                return node
            if key < node.key:
                node = node.left
            else:
                node = node.right
        return None
