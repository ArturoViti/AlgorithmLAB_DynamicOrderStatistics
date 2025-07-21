from DataStructure.Node.Node import Node

# @TODO: check with correct type
class BinarySearchTree:
    class _TreeNode:
        def __init__( self, node, left_node=None, right_node=None ):
            if ( not isinstance(node, Node) or (left_node is not None and not isinstance(left_node, Node))
                    or (right_node is not None and not isinstance(right_node, Node)) ):
                raise TypeError("Node must be of type DataStructure.Node.Node")

            self.node = node
            self.left_node = left_node
            self.right_node = right_node

    def __init__(self, node):
        if not isinstance(node, Node):
            raise TypeError("Node must be of type DataStructure.Node.Node")
        self.root = self._TreeNode(node)

    def insert(self, node):
        if not isinstance(node, Node):
            raise TypeError("Node must be of type DataStructure.Node.Node")
        self._insert_recursive(self.root, node)

    def _insert_recursive(self, current_tree_node, new_node):
        if new_node.getValue() < current_tree_node.node.getValue():
            if current_tree_node.left_node is None:
                current_tree_node.left_node = self._TreeNode(new_node)
            else:
                self._insert_recursive(current_tree_node.left_node, new_node)
        else:
            if current_tree_node.right_node is None:
                current_tree_node.right_node = self._TreeNode(new_node)
            else:
                self._insert_recursive(current_tree_node.right_node, new_node)

    def inorder(self, root):
        if root is None:
            return []
        return self.inorder(root.left_node) + [str(root.node.getValue())] + self.inorder(root.right_node)

    def __str__(self):
        return " -> ".join(self.inorder(self.root))
