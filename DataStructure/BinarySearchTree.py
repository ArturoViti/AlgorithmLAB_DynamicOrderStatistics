from DataStructure.Node.Node import Node
from DataStructure.Node.TreeNode import TreeNode
from DataStructure.OrderStatisticsStructure import OrderStatisticStructure


class BinarySearchTree(OrderStatisticStructure):
    """
        BinarySearchTree implements a classic binary search tree (BST) structure
        using TreeNode instances to maintain a sorted hierarchical organization
        of Node values.

        Attributes:
            __root (TreeNode): The root node of the binary search tree.
    """

    def __init__( self, value: int|None = None ):
        if value is None:
            self.__root = None
        else:
            if not isinstance(value, int):
                raise TypeError("Value must be integer")
            self.__root = TreeNode(value)


    def getRoot(self) -> TreeNode:
        return self.__root


    def insert( self, root: TreeNode | None, value: int ) -> TreeNode:
        """
            Insert a new root into the binary search tree.

            Parameters:
                root (TreeNode): The root of tree.
                value (Int): The value that a node could have
        """
        if root is None:
            newerNode = TreeNode( value )
            if self.__root is None:
                self.__root = newerNode
            return newerNode

        if root.getValue() <= value:
            root.setRight( self.insert(root.getRight(), value) )
        else:
            root.setLeft( self.insert(root.getLeft(), value) )
        return root

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
        return self._tree_to_string(self.__root)


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
        result += " " * level + f"--> {node.getValue()}\n"
        result += self._tree_to_string(node.getLeft(), level + 1)
        return result

    def _subtree_size(self, node: TreeNode) -> int:
        """
            Return the size of the subtree rooted at `node`.

            Parameters:
                node (TreeNode): The root of the subtree.

            Returns:
                int: Number of nodes in the subtree.
        """
        if node is None:
            return 0
        return 1 + self._subtree_size(node.getLeft()) + self._subtree_size(node.getRight())

    # Order Statistics Algorithm
    def OSSelect( self, node: TreeNode, i: int ) -> TreeNode | None:
        """
            Return the i-th smallest node (with rank i in an inorder traversal)

            Parameters:
                node (TreeNode): The root of the subtree.
                i (int): Index

            Returns:
                TreeNode | None: The corresponding node or None if out of bounds.
        """
        if not node:
            return None
        left = node.getLeft()
        left_size = self._subtree_size(left)

        if i == left_size + 1:
            return node
        elif i <= left_size:
            return self.OSSelect(left, i)
        else:
            return self.OSSelect(node.getRight(), i - left_size - 1)

    def OSRank( self, node: TreeNode ) -> int:
        """
        Return the rank (0-based index in inorder traversal) of a given value in the BST.

        Parameters:
            node (TreeNode): The node to find the rank of.

        Returns:
            int: The rank (number of nodes with value < input value).
            :param node:
        """

        def _os_rank( node: TreeNode, x: int ) -> int:
            if node is None:
                return 0

            if node.getValue() <= x:
                return 1 + _os_rank(node.getLeft(), x) + _os_rank(node.getRight(), x)
            else:
                return _os_rank(node.getLeft(), x)

        return _os_rank(self.__root, node.getValue())