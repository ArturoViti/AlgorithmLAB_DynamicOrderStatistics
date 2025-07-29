from DataStructure.AVLTree import AVLTree
from DataStructure.BinarySearchTree import BinarySearchTree
from DataStructure.Node.AVLNode import AVLNode
from DataStructure.Node.ListNode import ListNode
from DataStructure.Node.Node import Node
from DataStructure.Node.TreeNode import TreeNode
from DataStructure.OrderedList import OrderedList
import random
import time
import sys
import traceback

if __name__ == '__main__':
    # Creating Data
    values = random.sample(range(1, 10001), 10000)
    ordered_list = OrderedList()
    binary_tree = BinarySearchTree()

    # Insert in Data Structure
    bstNode = None
    listNodes = []
    treeNodes = []
    avlNodes = []
    for value in values:
        ordered_list.insert(value)
        bstNode = binary_tree.insert( bstNode, value )
        listNodes.append( ListNode( value ) )
        treeNodes.append( TreeNode( value ) )

    # AVL
    avl_tree = AVLTree()
    root = None
    for val in values:
        root = avl_tree.insert(val, root)


    root_bst = binary_tree.getRoot()
    root_avl = avl_tree.getRoot()
    head_list = ordered_list.getHead()

    size = avl_tree.getRoot().getSize()

    select_queries = random.sample(range(1, 1001), 1000)
    rank_queries = random.sample(values, 1000)

    # OrderedList
    start = time.perf_counter()
    root = ordered_list.getHead()
    for k in select_queries:
        ordered_list.OSSelect(root, k)
    for x in listNodes:
        ordered_list.OSRank(x)
    end = time.perf_counter()
    print(f"OrderedList Time: {end - start:.6f} seconds")

    # BinarySearchTree
    start = time.perf_counter()
    root = binary_tree.getRoot()
    for k in select_queries:
        binary_tree.OSSelect(root, k)
    for x in treeNodes:
        binary_tree.OSRank(x)
    end = time.perf_counter()
    print(f"BinarySearchTree Time: {end - start:.6f} seconds")

    # AVLTree
    start = time.perf_counter()
    root = avl_tree.getRoot()
    for k in select_queries:
        avl_tree.OSSelect(root, k)
    for x in avlNodes:
         avl_tree.OSRank(x)
    end = time.perf_counter()
    print(f"AVLTree Time: {end - start:.6f} seconds")