from DataStructure.Node.Node import Node
from DataStructure.Node.TreeNode import TreeNode

class BinarySearchTree:
    """
        BinarySearchTree implements a classic binary search tree (BST) structure
        using TreeNode instances to maintain a sorted hierarchical organization
        of Node values.

        Attributes:
            root (TreeNode): The root node of the binary search tree.
    """

    def __init__( self, node: Node ):
        if not isinstance(node, Node):
            raise TypeError("Node must be of type DataStructure.Node.Node")
        self.root = TreeNode(node.getValue())


    def insert( self, node: Node ):
        """
            Insert a new node into the binary search tree.

            Parameters:
                node (Node): The node to be inserted.

            Raises:
                TypeError: If the provided node is not an instance of Node.
        """
        if not isinstance(node, Node):
            raise TypeError("Node must be of type DataStructure.Node.Node")
        self._insert_recursive(self.root, node)


    def _insert_recursive( self, current_node: TreeNode, new_node: Node ):
        """
            Helper method to insert a node into the BST recursively.

            Parameters:
                current_node (TreeNode): The current node in the recursion.
                new_node (Node): The node to be inserted.
        """
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


    def inorder( self, root: TreeNode ):
        """
            Perform an inorder traversal of the tree.

            Parameters:
                root (TreeNode): The root node to start the traversal from.

            Returns:
                list[str]: A list of node values (as strings) in ascending order.
        """

        if root is None:
            return []
        return self.inorder(root.getLeft()) + [str(root.getValue())] + self.inorder(root.getRight())



    def __str__(self):
        return self._tree_to_string(self.root)


    def _tree_to_string( self, node: TreeNode, level: int = 0 ) -> str:
        """
            Helper method to recursively build the string representation of the tree.

            Parameters:
                node (TreeNode): The current node.
                level (int): The current depth level in the tree (used for indentation).

            Returns:
                str: A partial string of the tree from the given node downward.
        """
        if node is None:
            return ""
        result = self._tree_to_string(node.getRight(), level + 1)
        result += "    " * level + f"--> {node.getValue()}\n"
        result += self._tree_to_string(node.getLeft(), level + 1)
        return result
