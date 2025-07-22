from DataStructure.Node.Node import Node


class TreeNode(Node):
    def __init__(self, value, left_node=None, right_node=None):
        super().__init__(value)
        self.__left_node = left_node
        self.__right_node = right_node

    def getLeft(self):
        return self.__left_node

    def getRight(self):
        return self.__right_node

    def setLeft(self, left_node):
        self.__left_node = left_node

    def setRight(self, right_node):
        self.__right_node = right_node