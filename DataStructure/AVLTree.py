from DataStructure.Node.Node import Node
from DataStructure.Node.AVLNode import AVLNode

class AVLTree:
    """
        AVLTree implements a self-balancing binary search tree using AVLNode.

        It maintains the AVL property: for every node, the difference in height
        between its left and right subtrees is at most 1.

        Attributes:
            __root (AVLNode): The root of the AVL tree.
    """

    def __init__(self, value: int|None = None ):
        if value is None:
            self.__root = None
        else:
            if not isinstance(value, int):
                raise TypeError("Value must be integer")
            self.__root = AVLNode(value)


    def getRoot(self) -> AVLNode:
        return self.__root


    @staticmethod
    def height( node: AVLNode ) -> int:
        if not node:
            return 0
        return node.getHeight()

    @staticmethod
    def size( node: AVLNode ) -> int:
        if not node:
            return 0
        return node.getSize()


    def balance( self, node: AVLNode ) -> int:
        """
            Compute the balance factor of the given node.

            Parameters:
                node (AVLNode): The node to compute the balance factor for.

            Returns:
                int: The balance factor (left height - right height).
        """

        if not node:
            return 0
        return self.height(node.getLeft()) - self.height(node.getRight())

    def insert(self, node: AVLNode | None, key: int) -> AVLNode:
        if node is None:
            newerNode = AVLNode(key)
            if self.__root is None:
                self.__root = newerNode
            return newerNode

        if key < node.getValue():
            child = self.insert(node.getLeft(), key)
            node.setLeft(child)
            child.setParent(node)
        elif key > node.getValue():
            child = self.insert(node.getRight(), key)
            node.setRight(child)
            child.setParent(node)
        else:
            return node

        # Update height and size
        node.setHeight(1 + max(self.height(node.getLeft()), self.height(node.getRight())))
        node.setSize(1 + self.size(node.getLeft()) + self.size(node.getRight()))

        # Rebalance
        balance = self.balance(node)

        # Left Left
        if balance > 1 and key < node.getLeft().getValue():
            new_root = self._right_rotate(node)
            if new_root.getParent() is None:
                self.__root = new_root
            return new_root

        # Right Right
        if balance < -1 and key > node.getRight().getValue():
            new_root = self._left_rotate(node)
            if new_root.getParent() is None:
                self.__root = new_root
            return new_root

        # Left Right
        if balance > 1 and key > node.getLeft().getValue():
            node.setLeft(self._left_rotate(node.getLeft()))
            node.getLeft().setParent(node)
            new_root = self._right_rotate(node)
            if new_root.getParent() is None:
                self.__root = new_root
            return new_root

        # Right Left
        if balance < -1 and key < node.getRight().getValue():
            node.setRight(self._right_rotate(node.getRight()))
            node.getRight().setParent(node)
            new_root = self._left_rotate(node)
            if new_root.getParent() is None:
                self.__root = new_root
            return new_root

        if node.getParent() is None:
            self.__root = node

        return node

    def _left_rotate( self, y: AVLNode ) -> AVLNode:
        """
            Perform a left rotation around the given node.

            Parameters:
                y (AVLNode): The root of the subtree to rotate.

            Returns:
                AVLNode: The new root of the rotated subtree.
        """
        x = y.getRight()
        T2 = x.getLeft()

        # Perform rotation
        x.setLeft(y)
        y.setRight(T2)

        x.setParent(y.getParent())
        y.setParent(x)
        if T2:
            T2.setParent(y)

        # Update heights
        y.setHeight( 1 + max(self.height(y.getLeft()), self.height(y.getRight())) )
        x.setHeight( 1 + max(self.height(x.getLeft()), self.height(x.getRight())) )

        # Update Sizes
        y.setSize( 1 + self.size(y.getLeft()) + self.size(y.getRight()) )
        x.setSize( 1 + self.size(x.getLeft()) + self.size(x.getRight()) )

        # Return new root
        return x


    def _right_rotate(self, x: AVLNode) -> AVLNode:
        """
            Perform a right rotation around the given node.

            Parameters:
                z (AVLNode): The root of the subtree to rotate.

            Returns:
                AVLNode: The new root of the rotated subtree.
        """
        y = x.getLeft()
        T2 = y.getRight()

        # Perform rotation
        y.setRight(x)
        x.setLeft(T2)

        y.setParent(x.getParent())
        x.setParent(y)
        if T2:
            T2.setParent(x)

        # Update heights
        x.setHeight( 1 + max(self.height(x.getLeft()), self.height(x.getRight())) )
        y.setHeight( 1 + max(self.height(y.getLeft()), self.height(y.getRight())) )

        # Update sizes
        x.setSize( 1 + self.size(x.getLeft()) + self.size(x.getRight()) )
        y.setSize( 1 + self.size(y.getLeft()) + self.size(y.getRight()) )

        return y


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
        rank = (node.getLeft().getSize() if node.getLeft() else 0) + 1

        if i == rank:
            return node
        elif i < rank:
            return self.OSSelect(node.getLeft(), i)
        else:
            return self.OSSelect(node.getRight(), i - rank)

    def OSRank(self, x: AVLNode) -> int:
        rank = (x.getLeft().getSize() if x.getLeft() else 0) + 1
        node = x

        while node != self.__root:
            parent = node.getParent()
            if node == parent.getRight():
                left_size = parent.getLeft().getSize() if parent.getLeft() else 0
                rank += left_size + 1
            node = parent

        return rank

