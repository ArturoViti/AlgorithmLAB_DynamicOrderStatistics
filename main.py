from DataStructure.AVLTree import AVLTree
from DataStructure.BinarySearchTree import BinarySearchTree
from DataStructure.Node.Node import Node
from DataStructure.Node.TreeNode import TreeNode
from DataStructure.Node.AVLNode import AVLNode
from DataStructure.OrderedList import OrderedList
import random
import time
from memory_profiler import memory_usage

# Benchmark function
def benchmark_select_rank(structure, select_func, rank_func, values, ranks):
    def run():
        for k in ranks:
            select_func(k)
        for node in values:
            rank_func(node)
    start = time.perf_counter()
    mem = memory_usage(run, max_usage=True)
    end = time.perf_counter()
    return end - start, mem

if __name__ == '__main__':
    # Creating Data
    nodes = [ Node(random.randint(1, 1000)) for _ in range(1000)]
    ordered_list = OrderedList()
    binary_tree = BinarySearchTree(nodes[0])
    avl_tree = AVLTree(nodes[0])

    # Insert in Data Structure
    first = True
    for node in nodes:
        ordered_list.insert(node)

        if not first:
            binary_tree.insert(node)
            #avl_tree.insert(node)
        else:
            first = False

    select_queries = [random.randint(1, len(nodes)) for _ in range(1000)]
    rank_queries = random.sample(nodes, 1000)

    # Benchmark OrderedList
    t1, m1 = benchmark_select_rank(
        ordered_list,
        ordered_list.OSSelect,
        ordered_list.OSRank,
        rank_queries,
        select_queries
    )

    # Benchmark BinarySearchTree
    t2, m2 = benchmark_select_rank(
        binary_tree,
        binary_tree.OSSelect,
        lambda n: binary_tree.OSRank(TreeNode(n.getValue())),
        rank_queries,
        select_queries
    )

    # Benchmark AVLTree
    '''t3, m3 = benchmark_select_rank(
        avl_tree,
        avl_tree.OSSelect,
        lambda n: avl_tree.OSRank(AVLNode(n.getValue())),
        rank_queries,
        select_queries
    )'''

    print("\n--- Results ---")
    print(f"OrderedList:     Time={t1:.2f}s, Memory={m1:.2f} MiB")
    print(f"BinarySearchTree:Time={t2:.2f}s, Memory={m2:.2f} MiB")
    #print(f"AVLTree:         Time={t3:.2f}s, Memory={m3:.2f} MiB")