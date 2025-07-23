from DataStructure.Node.TreeNode import TreeNode


class AVLNode(TreeNode):
    """
        AVLNoide class to represent a TreeNode but has a height and size to build AVL Data Structure
    """

    def __init__(self, value: int, left_node: Node = None, right_node: Node = None):
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

    def setLeft( self, left_node: Node ):
        self.__left_node = left_node

    def setRight( self, right_node: Node ):
        self.__right_node = right_node

    def setHeight( self, height: Node ):
        self.__height = height

    def setSize( self, size: int ):
        self.__size = size
