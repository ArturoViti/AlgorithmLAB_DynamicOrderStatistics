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
    def height(node: AVLNode):
        if not node:
            return 0
        return node.getHeight()


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


    def _insert_recursive(self, current_node: AVLNode, new_node: AVLNode) -> AVLNode:
        """
            Helper method to recursively insert a node and rebalance the subtree.

            Parameters:
                current_node (AVLNode): Current node in recursion.
                new_node (AVLNode): New node to be inserted.

            Returns:
                AVLNode: The root of the balanced subtree.
       """

        if not current_node:
            return new_node
        elif new_node < current_node:
            current_node.setLeft( self._insert_recursive(current_node.getLeft(), new_node) )
        else:
            current_node.setRight( self._insert_recursive(current_node.getRight(), new_node) )

        left_height = current_node.getLeft().getHeight() if current_node.getLeft() else 0
        right_height = current_node.getRight().getHeight() if current_node.getRight() else 0
        current_node.setHeight(1 + max(left_height, right_height))

        balance = self.balance(current_node)

        left_size = current_node.getLeft().getSize() if current_node.getLeft() else 0
        right_size = current_node.getRight().getSize() if current_node.getRight() else 0
        current_node.setSize(1 + left_size + right_size)

        # Left rotation
        if balance > 1 and new_node < current_node.getLeft():
            return self._right_rotate(current_node)

        # Right rotation
        if balance < -1 and new_node > current_node.getRight():
            return self._left_rotate(current_node)

        # Left-Right rotation
        if balance > 1 and new_node > current_node.getLeft():
            current_node.setLeft( self._left_rotate(current_node.getLeft()) )
            return self._right_rotate(current_node)

        # Right-Left rotation
        if balance < -1 and new_node < current_node.getRight():
            current_node.right = self._right_rotate(current_node.getRight())
            return self._left_rotate(current_node)

        return current_node


    def _left_rotate(self, z: AVLNode) -> AVLNode:
        """
            Perform a left rotation around the given node.

            Parameters:
                z (AVLNode): The root of the subtree to rotate.

            Returns:
                AVLNode: The new root of the rotated subtree.
        """

        y = z.getRight()
        T2 = y.getLeft()

        y.setLeft(z)
        z.setRight(T2)

        # Update heights
        z_left_height = z.getLeft().getHeight() if z.getLeft() else 0
        z_right_height = z.getRight().getHeight() if z.getRight() else 0
        z.setHeight(1 + max(z_left_height, z_right_height))

        y_left_height = y.getLeft().getHeight() if y.getLeft() else 0
        y_right_height = y.getRight().getHeight() if y.getRight() else 0
        y.setHeight(1 + max(y_left_height, y_right_height))

        # Update sizes
        z_left_size = z.getLeft().getSize() if z.getLeft() else 0
        z_right_size = z.getRight().getSize() if z.getRight() else 0
        z.setSize(1 + z_left_size + z_right_size)

        y_left_size = y.getLeft().getSize() if y.getLeft() else 0
        y_right_size = y.getRight().getSize() if y.getRight() else 0
        y.setSize(1 + y_left_size + y_right_size)

        return y


    def _right_rotate(self, z: AVLNode) -> AVLNode:
        """
            Perform a right rotation around the given node.

            Parameters:
                z (AVLNode): The root of the subtree to rotate.

            Returns:
                AVLNode: The new root of the rotated subtree.
        """

        y = z.getLeft()
        T3 = y.getRight()

        y.setRight(z)
        z.setLeft(T3)

        # Update heights
        z_left_height = z.getLeft().getHeight() if z.getLeft() else 0
        z_right_height = z.getRight().getHeight() if z.getRight() else 0
        z.setHeight(1 + max(z_left_height, z_right_height))

        y_left_height = y.getLeft().getHeight() if y.getLeft() else 0
        y_right_height = y.getRight().getHeight() if y.getRight() else 0
        y.setHeight(1 + max(y_left_height, y_right_height))

        # Update sizes
        z_left_size = z.getLeft().getSize() if z.getLeft() else 0
        z_right_size = z.getRight().getSize() if z.getRight() else 0
        z.setSize(1 + z_left_size + z_right_size)

        y_left_size = y.getLeft().getSize() if y.getLeft() else 0
        y_right_size = y.getRight().getSize() if y.getRight() else 0
        y.setSize(1 + y_left_size + y_right_size)

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
    def OSSelect( self, i: int ) -> Node:
        return self._os_select(self.root, i)

    def _os_select( self, node: AVLNode, i: int ) -> AVLNode | None:
        rank = (node.getLeft().size if node.getLeft() else 0) + 1

        if i == rank:
            return node
        elif i < rank:
            return self._os_select( node.getLeft(), i )
        else:
            return self._os_select( node.getRight(), i - rank )

    def OSRank( self, x: AVLNode ) -> int:
        rank = (x.getLeft().size if x.getLeft() else 0) + 1
        node = x
        # @TODO: Add Parent to AVL Node
        return 0
        # while node != self.root:
        #    if node == node.