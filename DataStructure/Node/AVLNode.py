from DataStructure.Node.Node import Node
from DataStructure.Node.TreeNode import TreeNode


class AVLNode(TreeNode):
    """
        AVLNode class to represent a TreeNode but has a height and size to build AVL Data Structure
    """

    def __init__(self, value: int, left_node: Node = None, right_node: Node = None):
        super().__init__(value)
        self.__left_node = left_node
        self.__right_node = right_node
        # Height of the subtree rooted in the node
        self.__height = 1
        # Number of nodes of the subtree rooted in the node
        self.__size = 1

    def getHeight(self):
        return self.__height

    def getSize(self):
        return self.__size

    def setHeight( self, height: int ):
        self.__height = height

    def setSize( self, size: int ):
        self.__size = size
