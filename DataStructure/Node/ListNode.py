from DataStructure.Node.Node import Node


class ListNode(Node):
    """
        ListNode class to represent a Node but has a next node "pointer"
    """

    def __init__( self, value: int, next_node: Node = None ):
        super().__init__(value)
        self.__next = next_node

    def getNext(self):
        return self.__next

    def setNext( self, next_node: Node ):
        self.__next = next_node