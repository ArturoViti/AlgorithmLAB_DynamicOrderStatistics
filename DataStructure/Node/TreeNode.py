from DataStructure.Node.Node import Node


class TreeNode(Node):
    """
        TreeNode class to represent a Node but has a left node and right node "pointers" to build Tree Data Structure
    """

    def __init__( self, value: int , left_node: Node = None, right_node: Node = None ):
        super().__init__(value)
        self.__left_node = left_node
        self.__right_node = right_node
        self.__parent = None

    def getLeft(self):
        return self.__left_node

    def getRight(self):
        return self.__right_node

    def getParent(self):
        return self.__parent

    def setLeft( self, left_node: "TreeNode" ):
        self.__left_node = left_node
        if left_node:
            left_node.setParent(self)

    def setRight( self, right_node: "TreeNode" ):
        self.__right_node = right_node
        if right_node:
            right_node.setParent(self)

    def setParent( self, parent: "TreeNode" ):
        self.__parent = parent
