from DataStructure.AVLTree import AVLTree
from DataStructure.BinarySearchTree import BinarySearchTree
from DataStructure.Node.Node import Node
from DataStructure.OrderedList import OrderedList


def OrderedListTestOSSelectOSSRank():
    values = [20, 10, 30, 5, 15, 25, 35]
    ordered_list = OrderedList()
    for v in values:
        ordered_list.insert(v)

    print("Ordered List:")
    print(ordered_list)

    inorder_expected = sorted(values)

    print("\nOSSelect Test:")
    selected_nodes = []
    firstNode = ordered_list.getHead()

    for i in range(1, len(inorder_expected) + 1):
        node = ordered_list.OSSelect(firstNode, i)
        print(f"OSSelect({i}) -> {node.getValue()}")
        assert node.getValue() == inorder_expected[i - 1], f"❌ Error on OSSelect({i})"
        selected_nodes.append(node)

    print("\nTest OSRank:")
    for idx, node in enumerate(selected_nodes):
        rank = ordered_list.OSRank(node)
        print(f"OSRank({node.getValue()}) -> {rank}")
        assert rank == idx + 1, f"❌ Error on OSRank({node.getValue()})"

    print("\n ✅ All Ordered List Tests of OSSelect and OSRank Passed")


def BSTTestOSSelectOSSRank():
    # Create tree
    values = [20, 10, 30, 5, 15, 25, 35]
    root = None
    bst = BinarySearchTree()
    for v in values:
        root= bst.insert(root, v)

    print("BST:")
    print(bst)

    print("\nOSSelect Test:")
    # Order and select value
    inorder_expected = sorted(values)
    startRoot = bst.getRoot()
    print(bst)
    for i in range(1, len(values) + 1):
        # i-th the smallest key...
        node = bst.OSSelect(startRoot, i)
        print(f"OSSelect({i}):", node.getValue())
        assert node.getValue() == inorder_expected[i - 1], f"❌ Error on OSSelect({i})"

    print("\nOSRank Test:")
    def findNodeByValueHelper(tree_node, value):
        if not tree_node:
            return None
        if value == tree_node.getValue():
            return tree_node
        elif value < tree_node.getValue():
            return findNodeByValueHelper(tree_node.getLeft(), value)
        else:
            return findNodeByValueHelper(tree_node.getRight(), value)

    for idx, value in enumerate(inorder_expected):
        node = findNodeByValueHelper(startRoot, value)
        rank = bst.OSRank(node)
        print(f"OSRank({value}):", rank)
        print(f"Index + 1 ({value}):", idx + 1 )

        assert rank == idx + 1, f"❌ Error on OSRank({value})"

    print("\n ✅ All BST Tests of OSSelect and OSRank Passed")


def AVLTreeTestOSSelectOSSRank():
    values = [20, 10, 30, 5, 15, 25, 35, 1, 4, 6, 9, 2, 11, 12, 22, 45, 33, 56]
    root = None
    avl = AVLTree()
    for v in values:
        root = avl.insert(v, root)

    print("AVL Tree:")
    print(avl)

    inorder_expected = sorted(values)
    print("\nOSSelect Test:")
    root = avl.getRoot()
    for i in range(1, len(values) + 1):
        print(i)
        node = avl.OSSelect(root, i)
        print(node)
        print(f"OSSelect({i}) -> {node.getValue()}")
        print("On Expected({i}) -> ", inorder_expected[i - 1])
        assert node.getValue() == inorder_expected[i - 1], f"❌ Error on OSSelect({i})"

    def findNodeByValueHelper(avl_node, value):
        if not avl_node:
            return None
        if value == avl_node.getValue():
            return avl_node
        elif value < avl_node.getValue():
            return findNodeByValueHelper(avl_node.getLeft(), value)
        else:
            return findNodeByValueHelper(avl_node.getRight(), value)

    print("\nOSRank Test:")
    for idx, value in enumerate(inorder_expected):
        node = findNodeByValueHelper(root, value)
        rank = avl.OSRank(node)
        print(f"OSRank({value}) -> {rank}")
        assert rank == idx + 1, f"❌ Error on OSRank({value})"

    print("\n ✅ All AVL Tree Tests of OSSelect and OSRank Passed")


OrderedListTestOSSelectOSSRank()
BSTTestOSSelectOSSRank()
AVLTreeTestOSSelectOSSRank()