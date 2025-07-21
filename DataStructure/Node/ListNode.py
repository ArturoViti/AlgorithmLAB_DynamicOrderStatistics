from DataStructure.Node.Node import Node


class ListNode(Node):
    def __init__(self, value, next_node=None):
        super().__init__(value)
        self.__next = next_node

    def getNext(self):
        return self.__next

    def setNext(self, next_node):
        self.__next = next_node