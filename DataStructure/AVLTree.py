from DataStructure.Node.Node import Node
from DataStructure.Node.AVLNode import AVLNode

class AVLTree:
    """
        AVLTree implements a self-balancing binary search tree using AVLNode.

        It maintains the AVL property: for every node, the difference in height
        between its left and right subtrees is at most 1.

        Attributes:
            root (AVLNode): The root of the AVL tree.
    """

    def __init__(self, node):
        if not isinstance(node, Node):
            raise TypeError("Node must be of type DataStructure.Node.Node")
        self.root = AVLNode(node.getValue())


    @staticmethod
    def height( node: AVLNode ):
        if not node:
            return 0
        return node.getHeight()

    @staticmethod
    def size( node: AVLNode ):
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


    def insert( self, node ) -> None:
        """
            Insert a new node into the AVL tree, rebalancing if necessary.

            Parameters:
                node (Node): The node to insert.

            Raises:
                TypeError: If the input is not an instance of Node.
        """

        if not isinstance(node, Node):
            raise TypeError("Node must be of type DataStructure.Node.Node")
        avl_node = AVLNode(node.getValue())
        self.root = self._insert_recursive(self.root, avl_node)


    def _insert_recursive(self, current: AVLNode, new_node: AVLNode) -> AVLNode:
        """
            Helper method to recursively insert a node and rebalance the subtree.

            Parameters:
                current_node (AVLNode): Current node in recursion.
                new_node (AVLNode): New node to be inserted.

            Returns:
                AVLNode: The root of the balanced subtree.
       """

        if current is None:
            return new_node

        if new_node <= current:
            current.setLeft(self._insert_recursive(current.getLeft(), new_node))
        elif new_node > current:
            current.setRight(self._insert_recursive(current.getRight(), new_node))
        else:
            return current

        left = current.getLeft()
        right = current.getRight()
        lh = left.getHeight() if left else 0
        rh = right.getHeight() if right else 0
        current.setHeight(1 + max(lh, rh))

        ls = left.getSize() if left else 0
        rs = right.getSize() if right else 0
        current.setSize(1 + ls + rs)

        balance = lh - rh

        # LL
        if balance > 1 and new_node < left:
            return self._right_rotate(current)
        # RR
        if balance < -1 and new_node > right:
            return self._left_rotate(current)
        # LR
        if balance > 1 and new_node > left:
            current.setLeft(self._left_rotate(left))
            return self._right_rotate(current)
        # RL
        if balance < -1 and new_node < right:
            current.setRight(self._right_rotate(right))
            return self._left_rotate(current)

        return current


    def _left_rotate(self,y: AVLNode) -> AVLNode:
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
        return self._tree_to_string(self.root)

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
    def OSSelect( self, i: int ) -> AVLNode:
        return self._os_select(self.root, i)

    def _os_select( self, node: AVLNode, i: int ) -> AVLNode | None:
        rank = (node.getLeft().getSize() if node.getLeft() else 0) + 1

        if i == rank:
            return node
        elif i < rank:
            return self._os_select( node.getLeft(), i )
        else:
            return self._os_select( node.getRight(), i - rank )


    def OSRank( self, x: AVLNode ) -> int:
        rank = (x.getLeft().getSize() if x.getLeft() else 0) + 1
        node = x

        while node != self.root:
           if node == node.getParent().getRight():
               rank += node.getParent().getLeft().getSize() + 1
           node = node.getParent()

        return rank
