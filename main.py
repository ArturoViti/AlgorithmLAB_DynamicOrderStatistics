from DataStructure.AVLTree import AVLTree
from DataStructure.BinarySearchTree import BinarySearchTree
from DataStructure.Node.AVLNode import AVLNode
from DataStructure.Node.ListNode import ListNode
from DataStructure.Node.Node import Node
from DataStructure.Node.TreeNode import TreeNode
from DataStructure.OrderedList import OrderedList
from Plot.PlotManager import PlotManager
import random
import time
import sys
import traceback
from pympler import asizeof


# Sizes
def get_list_memory_usage(head):
    total_size = 0
    visited = set()
    current = head
    while current is not None:
        if id(current) in visited:
            break
        visited.add(id(current))
        size_node = sys.getsizeof(current)
        total_size += size_node
        current = current.getNext()

    return total_size

if __name__ == '__main__':
    VALUES_NUMBER = 10000
    TRIES_NUMBER = 1000

    # Creating Data
    values = random.sample(range(1, VALUES_NUMBER + 1), VALUES_NUMBER)
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
        avlNodes.append(root)


    root_bst = binary_tree.getRoot()
    root_avl = avl_tree.getRoot()
    head_list = ordered_list.getHead()

    size = avl_tree.getRoot().getSize()

    select_queries = random.sample(range(1, TRIES_NUMBER + 1), TRIES_NUMBER)
    rank_queries = random.sample(values, TRIES_NUMBER )

    head = ordered_list.getHead()
    mem_usage = get_list_memory_usage(head)

    memory_usage_ordered_list = mem_usage
    memory_usage_binary_tree = asizeof.asizeof(binary_tree)
    memory_usage_avl_tree = asizeof.asizeof(avl_tree)
    print(f"Memory used by OrderedList: {memory_usage_ordered_list:,} bytes")
    print(f"Memory used by BinarySearchTree: {memory_usage_binary_tree:,} bytes")
    print(f"Memory used by AVLTree: {memory_usage_avl_tree:,} bytes")
    # ... Make plot
    PlotManager.saveMemoryUsagePlot({
        "OrderedList": memory_usage_ordered_list,
        "BinarySearchTree": memory_usage_binary_tree,
        "AVLTree": memory_usage_avl_tree
    })

    times_osselect = {}
    times_osrank = {}

    # OrderedList
    root = ordered_list.getHead()
    start = time.perf_counter()
    for k in select_queries:
        ordered_list.OSSelect(root, k)
    end = time.perf_counter()
    print(f"OrderedList Time OSSelect of {TRIES_NUMBER} values: {end - start:.6f} seconds")
    times_osselect["OrderedList"] = end - start
    start = time.perf_counter()
    for x in listNodes:
        ordered_list.OSRank(x)
    end = time.perf_counter()
    print(f"OrderedList Time OSSrank of {TRIES_NUMBER} nodes: {end - start:.6f} seconds")
    times_osrank["OrderedList"] = end - start


    # BinarySearchTree
    root = binary_tree.getRoot()
    start = time.perf_counter()
    for k in select_queries:
        binary_tree.OSSelect(root, k)
    end = time.perf_counter()
    print(f"BinarySearchTree Time OSSelect of {TRIES_NUMBER} values: {end - start:.6f} seconds")
    times_osselect["BinarySearchTree"] = end - start
    start = time.perf_counter()
    for x in treeNodes:
        binary_tree.OSRank(x)
    end = time.perf_counter()
    print(f"BinarySearchTree Time OSSrank of {TRIES_NUMBER} nodes: {end - start:.6f} seconds")
    times_osrank["BinarySearchTree"] = end - start

    # AVLTree
    root = avl_tree.getRoot()
    start = time.perf_counter()
    for k in select_queries:
        avl_tree.OSSelect(root, k)
    end = time.perf_counter()
    times_osselect["AVLTree"] = end - start
    print(f"AVLTree Time OSSelect of {TRIES_NUMBER} values: {end - start:.6f} seconds")
    start = time.perf_counter()
    for x in avlNodes:
         avl_tree.OSRank(x)
    end = time.perf_counter()
    print(f"AVLTree Time OSSrank of {TRIES_NUMBER} nodes: {end - start:.6f} seconds")
    times_osrank["AVLTree"] = end - start

    # Plot Times Stats
    PlotManager.saveOSSelectTimePlot( times_osselect, TRIES_NUMBER )
    PlotManager.saveOSRankTimePlot( times_osrank, TRIES_NUMBER )