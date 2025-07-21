from DataStructure.Node.Node import Node
from DataStructure.Node.ListNode import ListNode

class OrderedList:
    def __init__(self):
        self.head = None

    def insert(self, new_node):
        if not isinstance(new_node, Node):
            raise TypeError("Node must be of type DataStructure.Node.Node")

        new_list_node = ListNode(new_node.getValue())

        if self.head is None or new_node < self.head:
            new_list_node.setNext(self.head)
            self.head = new_list_node
            return

        current = self.head
        while current.getNext() is not None and current.getNext() < new_node:
            current = current.next

        new_list_node.setNext(current.getNext())
        current.setNext(new_list_node)

    def __str__(self):
        values = []
        current = self.head
        while current is not None:
            values.append(str(current.getValue()))
            current = current.getNext()
        return " -> ".join(values)