from DataStructure.AVLTree import AVLTree
from DataStructure.BinarySearchTree import BinarySearchTree
from DataStructure.Node.Node import Node
from DataStructure.OrderedList import OrderedList


def OrderedListTestOSSelectOSSRank():
    values = [20, 10, 30, 5, 15, 25, 35]
    ordered_list = OrderedList()
    for v in values:
        ordered_list.insert(Node(v))

    print("Ordered List:")
    print(ordered_list)

    inorder_expected = sorted(values)

    print("\nOSSelect Test:")
    selected_nodes = []
    for i in range(1, len(inorder_expected) + 1):
        node = ordered_list.OSSelect(i)
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
    bst = BinarySearchTree(Node(values[0]))
    for v in values[1:]:
        bst.insert(Node(v))

    print("BST:")
    print(bst)

    print("\nOSSelect Test:")
    # Order and select value
    inorder_expected = sorted(values)
    for i in range(1, len(values) + 1):
        # i-th the smallest key...
        node = bst.OSSelect(i)
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
        node = findNodeByValueHelper(bst.root, value)
        rank = bst.OSRank(node)
        print(f"OSRank({value}):", rank)
        assert rank == idx + 1, f"❌ Error on OSRank({value})"

    print("\n ✅ All BST Tests of OSSelect and OSRank Passed")


def AVLTreeTestOSSelectOSSRank():
    values = [20, 10, 30, 5, 15, 25, 35]
    avl = AVLTree(Node(values[0]))
    for v in values[1:]:
        avl.insert(Node(v))

    print("AVL Tree:")
    print(avl)

    inorder_expected = sorted(values)
    print("\nOSSelect Test:")
    for i in range(1, len(values) + 1):
        node = avl.OSSelect(i)
        print(f"OSSelect({i}) -> {node.getValue()}")
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
        node = findNodeByValueHelper(avl.root, value)
        rank = avl.OSRank(node)
        print(f"OSRank({value}) -> {rank}")
        assert rank == idx + 1, f"❌ Error on OSRank({value})"

    print("\n ✅ All AVL Tree Tests of OSSelect and OSRank Passed")


OrderedListTestOSSelectOSSRank()
BSTTestOSSelectOSSRank()
AVLTreeTestOSSelectOSSRank()