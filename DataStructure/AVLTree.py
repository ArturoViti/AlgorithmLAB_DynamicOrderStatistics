from DataStructure.BinarySearchTree import BinarySearchTree
from DataStructure.Node.AVLNode import AVLNode

class AVLTree(BinarySearchTree):
    """
        AVLTree implements a self-balancing binary search tree using AVLNode.

        It maintains the AVL property: for every node, the difference in height
        between its left and right subtrees is at most 1.

        Attributes:
            __root (AVLNode): The root of the AVL tree.
    """

    def __init__(self, value: int | None = None):
        super().__init__(value)
        self.__root = AVLNode(value) if value is not None else None

    def getRoot(self) -> AVLNode:
        return self.__root

    @staticmethod
    def height(node: AVLNode) -> int:
        return node.getHeight() if node else 0

    @staticmethod
    def size(node: AVLNode) -> int:
        return node.getSize() if node else 0

    def balance( self, node: AVLNode ) -> int:
        """
            Compute the balance factor of the given node.

            Parameters:
                node (AVLNode): The node to compute the balance factor for.

            Returns:
                int: The balance factor (left height - right height).
        """
        return self.height(node.getLeft()) - self.height(node.getRight()) if node else 0



    def insert(self, key: int, node: AVLNode | None = None) -> AVLNode:
        """
            Insert a key into the AVL tree.

            If no node is provided, insertion begins at the tree's root.
            Updates the root reference if necessary.

            Parameters:
                key (int): The value to insert into the tree.
                node (AVLNode, optional): The starting node for insertion. Defaults to None.

            Returns:
                AVLNode: The updated root of the subtree after insertion.
        """
        if node is None:
            node = self.__root
        node = self._insert(node, key)
        self.__root = node
        return node


    def _insert(self, node: AVLNode | None, key: int) -> AVLNode:
        """
            Recursively insert a key into the AVL tree and rebalance the tree if needed.

            This method updates the height and size of nodes and performs the necessary
            rotations to maintain AVL balance.

            Parameters:
                node (AVLNode | None): The root of the current subtree.
                key (int): The value to insert.

            Returns:
                AVLNode: The updated node after insertion and rebalancing.
        """
        if node is None:
            return AVLNode(key)

        if key < node.getValue():
            node.setLeft(self._insert(node.getLeft(), key))
            node.getLeft().setParent(node)
        elif key > node.getValue():
            node.setRight(self._insert(node.getRight(), key))
            node.getRight().setParent(node)
        else:
            return node

        node.setHeight(1 + max(self.height(node.getLeft()), self.height(node.getRight())))
        node.setSize(1 + self.size(node.getLeft()) + self.size(node.getRight()))

        balance = self.balance(node)

        if balance > 1:
            if key < node.getLeft().getValue():
                return self._right_rotate(node)
            else:
                node.setLeft(self._left_rotate(node.getLeft()))
                return self._right_rotate(node)

        if balance < -1:
            if key > node.getRight().getValue():
                return self._left_rotate(node)
            else:
                node.setRight(self._right_rotate(node.getRight()))
                return self._left_rotate(node)

        return node

    def _left_rotate( self, x: AVLNode ) -> AVLNode:
        """
            Perform a left rotation around the given node.

            Parameters:
                x (AVLNode): The root of the subtree to rotate.

            Returns:
                AVLNode: The new root of the rotated subtree.
        """
        y = x.getRight()
        T2 = y.getLeft()

        # Perform rotation
        y.setLeft(x)
        x.setRight(T2)

        y.setParent(x.getParent())
        x.setParent(y)
        if T2:
            T2.setParent(x)

        # Update heights
        x.setHeight( 1 + max(self.height(x.getLeft()), self.height(x.getRight())) )
        y.setHeight( 1 + max(self.height(y.getLeft()), self.height(y.getRight())) )

        # Update Sizes
        x.setSize( 1 + self.size(x.getLeft()) + self.size(x.getRight()) )
        y.setSize( 1 + self.size(y.getLeft()) + self.size(y.getRight()) )

        # Return new root
        return y


    def _right_rotate(self, y: AVLNode) -> AVLNode:
        """
            Perform a right rotation around the given node.

            Parameters:
                y (AVLNode): The root of the subtree to rotate.

            Returns:
                AVLNode: The new root of the rotated subtree.
        """
        x = y.getLeft()
        T2 = x.getRight()

        # Perform rotation
        x.setRight(y)
        y.setLeft(T2)

        x.setParent(y.getParent())
        y.setParent(x)
        if T2:
            T2.setParent(y)

        # Update heights
        y.setHeight( 1 + max(self.height(y.getLeft()), self.height(y.getRight())) )
        x.setHeight( 1 + max(self.height(x.getLeft()), self.height(x.getRight())) )

        # Update sizes
        y.setSize( 1 + self.size(y.getLeft()) + self.size(y.getRight()) )
        x.setSize( 1 + self.size(x.getLeft()) + self.size(x.getRight()) )

        return x


    def __str__(self) -> str:
        return self._tree_to_string(self.__root)

    def _tree_to_string( self, node: AVLNode, level = 0 ) -> str:
        """
            Helper method to generate a visual representation of the AVL tree.

            Parameters:
                node (AVLNode): The current node in the traversal.
                level (int): The depth level (used for indentation).

            Returns:
                str: A multiline string representing the subtree.
        """

        if node is None:
            return ""
        result = self._tree_to_string(node.getRight(), level + 1)
        result += "    " * level + f"--> { "V: " + str(node.getValue()) + ", H: " + str(node.getHeight()) + ", S: " 
            + str(node.getSize())}\n"
        result += self._tree_to_string(node.getLeft(), level + 1)
        return result


    # Order Statistics Algorithm
    def OSSelect( self, node: AVLNode, i: int ) -> AVLNode | None:
        """
            Return the i-th smallest node (with rank i in an inorder traversal), using size

            Parameters:
                node (TreeNode): The root of the subtree.
                i (int): Index

            Returns:
                TreeNode | None: The corresponding node or None if out of bounds.
        """
        if node is None:
            return None

        left_size = self.size(node.getLeft())
        rank = left_size + 1

        if i == rank:
            return node
        elif i < rank:
            return self.OSSelect(node.getLeft(), i)
        else:
            return self.OSSelect(node.getRight(), i - rank)


    def OSRank(self, x: AVLNode) -> int:
        """
            Return the rank (1-based index in inorder traversal) of node x, using size

            Parameters:
                x (AVLNode): The node whose rank we want to find.

            Returns:
                int: The rank of the node.
        """
        rank = self.size(x.getLeft()) + 1
        node = x

        while node != self.__root:
            parent = node.getParent()
            if node == parent.getRight():
                rank += self.size(parent.getLeft()) + 1
            node = parent

        return rank

    def tree_to_list_inorder(self, node: AVLNode | None, nodes: list[AVLNode] = None) -> list[AVLNode]:
        """
        Helper method to traverse the AVL tree and collect nodes in in-order.

        Parameters:
            node (AVLNode | None): The current node in the traversal.
            nodes (list[AVLNode], optional): Accumulator list for nodes.

        Returns:
            list[AVLNode]: List of AVL nodes in in-order.
        """
        if nodes is None:
            nodes = []
        if node is not None:
            self.tree_to_list_inorder(node.getLeft(), nodes)
            nodes.append(node)
            self.tree_to_list_inorder(node.getRight(), nodes)
        return nodes