# This is a sample Python script.
from DataStructure.Node.ListNode import ListNode
from DataStructure.Node import Node
from DataStructure.OrderedList import OrderedList


# Press ⇧F10 to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press ⌘F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    orderedList = OrderedList()
    orderedList.insert( Node(4) )
    orderedList.insert( ListNode(8) )
    orderedList.insert( ListNode(4) )
    print(orderedList)

    # tree = BinarySearchTree(Node(4))
    # tree.insert( Node(8) )
    # print(tree)
# See PyCharm help at https://www.jetbrains.com/help/pycharm/
