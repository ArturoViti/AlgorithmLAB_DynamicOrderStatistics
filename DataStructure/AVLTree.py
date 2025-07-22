from DataStructure.Node.Node import Node
from DataStructure.Node.AVLNode import AVLNode

class AVLTree:
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
        if not node:
            return 0
        return self.height(node.getLeft()) - self.height(node.getRight())

    def insert(self, node):
        if not isinstance(node, Node):
            raise TypeError("Node must be of type DataStructure.Node.Node")
        avl_node = AVLNode(node.getValue())
        self.root = self._insert_recursive(self.root, avl_node)

    def _insert_recursive(self, current_node: AVLNode, new_node: AVLNode) -> AVLNode:
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

    def _left_rotate(self, z: AVLNode):
        y = z.getRight()
        T2 = y.getLeft()

        y.setLeft(z)
        z.setRight(T2)

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

    def _right_rotate(self, z: AVLNode):
        y = z.getLeft()
        T3 = y.getRight()

        y.setRight(z)
        z.setLeft(T3)

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

    def inorder(self, root):
        if root is None:
            return []
        return ( self.inorder(root.getLeft()) + [str(root.getValue())] + self.inorder(root.getRight()) )

    def __str__(self):
        return self._tree_to_string(self.root)

    def _tree_to_string(self, node, level=0):
        if node is None:
            return ""
        result = self._tree_to_string(node.getRight(), level + 1)
        result += "    " * level + f"--> { "V: " + str(node.getValue()) + ", H: " + str(node.getHeight()) + ", S: " 
            + str(node.getSize())}\n"
        result += self._tree_to_string(node.getLeft(), level + 1)
        return result
