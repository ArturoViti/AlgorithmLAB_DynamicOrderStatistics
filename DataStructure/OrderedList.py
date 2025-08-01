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
        self.__head = None


    def getHead(self) -> ListNode:
        return self.__head


    def insert( self, value: int ) -> None:
        """
            Insert a new node into the ordered list, maintaining ascending order.

            The method creates a new ListNode from the provided Node's value and inserts it
            at the correct position so that the list remains sorted in ascending order.

            Parameters:
                value (int): The value to insert as ListNode

            Raises:
                TypeError: If new_node is not an instance of Node.

            Returns:
                None
        """

        if not isinstance(value, int):
            raise TypeError("Value must be Integer")

        new_list_node = ListNode(value)

        if self.__head is None or new_list_node <= self.__head:
            new_list_node.setNext(self.__head)
            self.__head = new_list_node
            return

        current = self.__head
        while current.getNext() is not None and current.getNext() <= new_list_node:
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
        current = self.__head
        while current is not None:
            values.append(str(current.getValue()))
            current = current.getNext()
        return " -> ".join(values)


    # Order Statistics Algorithm
    def OSSelect( self, node: ListNode, i: int ) -> ListNode:
        """
            Return the i-th smallest node. List is ordered, so simply iterate through

            Parameters:
                node (ListNode): The start of OrderedList
                i (int): Index

            Returns:
                ListNode | None: The corresponding node or None if out of bounds.
        """
        if i < 1:
            raise IndexError("Index must be >= 1")

        current = node
        position = 1

        while current is not None:
            if position == i:
                return current
            current = current.getNext()
            position += 1

        raise IndexError("Index out of range")

    def OSRank( self, x: ListNode ) -> int | None:
        """
            Return the rank (1-based index on iteration) of node x.

            Parameters:
                x (ListNode): The node whose rank we want to find.

            Returns:
                int: The rank of the node, index of Ordered List
        """
        current = self.__head
        position = 1

        while current is not None:
            if current == x:
                return position
            current = current.getNext()
            position += 1

        return None