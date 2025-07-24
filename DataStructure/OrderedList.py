from typing import Any

from DataStructure.Node.Node import Node
from DataStructure.Node.ListNode import ListNode
from DataStructure.OrderStatisticsStructure import OrderStatisticStructure


class OrderedList(OrderStatisticStructure):
    """
        OrderedList is a linked list of Node elements, where each node points to the next one,
        maintaining the elements in ascending order by value.

        Each element of the OrderedList is itself an instance of OrderedList.
    """

    def __init__(self):
        self.head = None


    def insert( self, new_node: Node ) -> None:
        """
            Insert a new node into the ordered list, maintaining ascending order.

            The method creates a new ListNode from the provided Node's value and inserts it
            at the correct position so that the list remains sorted in ascending order.

            Parameters:
                new_node (Node): The node to insert. Must be an instance of Node.

            Raises:
                TypeError: If new_node is not an instance of Node.

            Returns:
                None
        """
        if not isinstance(new_node, Node):
            raise TypeError("Node must be of type DataStructure.Node.Node")

        new_list_node = ListNode(new_node.getValue())

        if self.head is None or new_node < self.head:
            new_list_node.setNext(self.head)
            self.head = new_list_node
            return

        current = self.head
        while current.getNext() is not None and current.getNext() < new_node:
            current = current.getNext()

        new_list_node.setNext(current.getNext())
        current.setNext(new_list_node)


    def __str__(self):
        """
            Return a string representation of the ordered list.

            Traverses the list from head to tail, collecting node values in order,
            and returns them as a string separated by ' -> '.

            Returns:
                str: A string showing the ordered sequence of node values.
        """
        values = []
        current = self.head
        while current is not None:
            values.append(str(current.getValue()))
            current = current.getNext()
        return " -> ".join(values)

    # Order Statistics Algorithm
    def OSSelect( self, i: int ) -> Node:
        if i < 1:
            raise IndexError("Index must be >= 1")

        current = self.head
        position = 1

        while current is not None:
            if position == i:
                return current
            current = current.getNext()
            position += 1

        raise IndexError("Index out of range")

    def OSRank( self, x: ListNode ) -> int | None:
        current = self.head
        position = 1

        while current is not None:
            if current == x:
                return position
            current = current.getNext()
            position += 1

        return None