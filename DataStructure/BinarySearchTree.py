from DataStructure.Node.Node import Node
from DataStructure.Node.TreeNode import TreeNode

class BinarySearchTree:
    def __init__(self, node):
        if not isinstance(node, Node):
            raise TypeError("Node must be of type DataStructure.Node.Node")
        self.root = TreeNode(node.getValue())

    def insert(self, node):
        if not isinstance(node, Node):
            raise TypeError("Node must be of type DataStructure.Node.Node")
        self._insert_recursive(self.root, node)

    def _insert_recursive(self, current_node, new_node):
        if new_node < current_node:
            if current_node.getLeft() is None:
                current_node.setLeft(TreeNode(new_node.getValue()))
            else:
                self._insert_recursive( current_node.getLeft(), new_node)
        else:
            if current_node.getRight() is None:
                current_node.setRight(TreeNode(new_node.getValue()))
            else:
                self._insert_recursive(current_node.getRight(), new_node)

    def inorder(self, root):
        if root is None:
            return []
        return (
            self.inorder(root.getLeft())
            + [str(root.getValue())]
            + self.inorder(root.getRight())
        )

    def __str__(self):
        return self._tree_to_string(self.root)

    def _tree_to_string(self, node, level=0):
        if node is None:
            return ""
        result = self._tree_to_string(node.getRight(), level + 1)
        result += "    " * level + f"--> {node.getValue()}\n"
        result += self._tree_to_string(node.getLeft(), level + 1)
        return result
