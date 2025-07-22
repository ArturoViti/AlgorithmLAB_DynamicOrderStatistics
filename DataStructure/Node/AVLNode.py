from DataStructure.Node.TreeNode import TreeNode


class AVLNode(TreeNode):
    def __init__(self, value, left_node=None, right_node=None):
        super().__init__(value)
        self.__left_node = left_node
        self.__right_node = right_node
        # Height of the subtree rooted in the node
        self.__height = 1
        # Number of nodes of the subtree rooted in the node
        self.__size = 1

    def getLeft(self):
        return self.__left_node

    def getRight(self):
        return self.__right_node

    def getHeight(self):
        return self.__height

    def getSize(self):
        return self.__size

    def setLeft(self, left_node):
        self.__left_node = left_node

    def setRight(self, right_node):
        self.__right_node = right_node

    def setHeight(self, height):
        self.__height = height

    def setSize(self, size):
        self.__size = size
