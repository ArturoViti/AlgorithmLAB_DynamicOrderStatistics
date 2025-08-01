from DataStructure.AVLTree import AVLTree
from DataStructure.BinarySearchTree import BinarySearchTree
from DataStructure.Node.ListNode import ListNode
from DataStructure.Node.TreeNode import TreeNode
from DataStructure.OrderedList import OrderedList
from Plot.PlotManager import PlotManager
import random
import time
import sys
from pympler import asizeof


# Sizes
def get_list_memory_usage(head):
    """
        Calculate the total memory usage of a linked list.

        This method traverses a singly linked list starting from the given head node
        and sums the memory size of each node using sys.getsizeof. It ensures that
        each node is counted only once, even in the presence of cycles, by tracking
        visited nodes.

        Parameters:
            head (object): The head node of the linked list. Each node is expected to
                           implement a getNext() method to access the next node.

        Returns:
            int: The total memory usage in bytes of all visited nodes.
    """
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
    TRIALS_PER_N = 0
    N_VALUES = [1000, 2000, 4000, 6000, 8000, 10000]

    osselect_results = {}
    osrank_results = {}

    for VALUES_NUMBER in N_VALUES:
        print(f"\n--- Running tests for n = {VALUES_NUMBER} ---")

        # Data
        values = random.sample(range(1, VALUES_NUMBER + 1), VALUES_NUMBER)
        ordered_list = OrderedList()
        binary_tree = BinarySearchTree()
        avl_tree = AVLTree()

        listNodes = []
        treeNodes = []
        avlNodes = []

        bstNode = None
        root_avl = None

        for value in values:
            ordered_list.insert(value)
            bstNode = binary_tree.insert(binary_tree.getRoot(), value)
            listNodes.append(ListNode(value))
            treeNodes.append(bstNode)
            root_avl = avl_tree.insert(value, root_avl)
            avlNodes.append(root_avl)

        # Select only half of total
        TRIALS_PER_N = VALUES_NUMBER
        select_queries = random.sample(range(1, TRIALS_PER_N + 1), TRIALS_PER_N)

        # Size Calculator on only MAX Size
        if VALUES_NUMBER == max(N_VALUES):
            memory_usage_ordered_list = get_list_memory_usage(ordered_list.getHead())
            memory_usage_binary_tree = asizeof.asizeof(binary_tree)
            memory_usage_avl_tree = asizeof.asizeof(avl_tree)
            print(f"Memory used by OrderedList: {memory_usage_ordered_list:,} bytes")
            print(f"Memory used by BinarySearchTree: {memory_usage_binary_tree:,} bytes")
            print(f"Memory used by AVLTree: {memory_usage_avl_tree:,} bytes")

            PlotManager.saveMemoryUsagePlot({
                "OrderedList": memory_usage_ordered_list,
                "BinarySearchTree": memory_usage_binary_tree,
                "AVLTree": memory_usage_avl_tree
            })

        # OSSelect & OSRank
        times_osselect = {}
        times_osrank = {}

        # OrderedList
        start = time.perf_counter()
        for k in select_queries:
            ordered_list.OSSelect(ordered_list.getHead(), k)
        times_osselect["OrderedList"] = time.perf_counter() - start
        print(f"OrderedList Time OSSelect of {len(select_queries)} values: {times_osselect["OrderedList"]:.6f} seconds")

        start = time.perf_counter()
        for x in listNodes:
            ordered_list.OSRank(x)
        times_osrank["OrderedList"] = time.perf_counter() - start
        print(f"OrderedList Time OSRank of {len(listNodes)} values: {times_osrank["OrderedList"]:.6f} seconds")

        # BinarySearchTree
        start = time.perf_counter()
        for k in select_queries:
            binary_tree.OSSelect(binary_tree.getRoot(), k)
        times_osselect["BinarySearchTree"] = time.perf_counter() - start
        print(f"BinarySearchTree Time OSSelect of {len(select_queries)} values: {times_osselect["BinarySearchTree"]:.6f} seconds")


        start = time.perf_counter()
        for x in treeNodes:
            binary_tree.OSRank(x)
        times_osrank["BinarySearchTree"] = time.perf_counter() - start
        print(f"BinarySearchTree Time OSRank of {len(treeNodes)} values: {times_osrank["BinarySearchTree"]:.6f} seconds")

        # AVLTree
        start = time.perf_counter()
        for k in select_queries:
            avl_tree.OSSelect(avl_tree.getRoot(), k)
        times_osselect["AVLTree"] = time.perf_counter() - start
        print(f"AVLTree Time OSSelect of {len(select_queries)} values: {times_osselect["AVLTree"]:.6f} seconds")


        start = time.perf_counter()
        for x in avlNodes:
            avl_tree.OSRank(x)
        times_osrank["AVLTree"] = time.perf_counter() - start
        print(f"AVLTree Time OSRank of {len(treeNodes)} values: {times_osrank["AVLTree"]:.6f} seconds")


        osselect_results[VALUES_NUMBER] = times_osselect
        osrank_results[VALUES_NUMBER] = times_osrank

    PlotManager.saveOSSelectTimePlot(osselect_results[max(N_VALUES)], TRIALS_PER_N)
    PlotManager.saveOSRankTimePlot(osrank_results[max(N_VALUES)], TRIALS_PER_N)
    PlotManager.saveOSOperationComplexityPlot(osselect_results, "OSSelect")
    PlotManager.saveOSOperationComplexityPlot(osrank_results, "OSRank")
