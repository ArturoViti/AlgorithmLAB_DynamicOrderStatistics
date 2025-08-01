import random

from DataStructure.AVLTree import AVLTree
from DataStructure.BinarySearchTree import BinarySearchTree
from DataStructure.OrderedList import OrderedList

def testOrderedList():
    # Test 1: Insert a single node
    ol = OrderedList()
    ol.insert(5)
    assert str(ol) == "5", f"❌ Test 1 Failed: got {str(ol)}"

    # Test 2: Insert nodes in ascending order
    ol = OrderedList()
    ol.insert(1)
    ol.insert(3)
    ol.insert(5)
    assert str(ol) == "1 -> 3 -> 5", f"❌ Test 2 Failed: got {str(ol)}"

    # Test 3: Insert nodes out of order
    ol = OrderedList()
    ol.insert(5)
    ol.insert(1)
    ol.insert(3)
    assert str(ol) == "1 -> 3 -> 5", f"❌ Test 3 Failed: got {str(ol)}"

    # Test 4: Insert duplicate values
    ol = OrderedList()
    ol.insert(3)
    ol.insert(3)
    ol.insert(3)
    assert str(ol) == "3 -> 3 -> 3", f"❌ Test 4 Failed: got {str(ol)}"

    # Test 5: Empty list
    ol = OrderedList()
    assert str(ol) == "", f"❌ Test 5 Failed: got {str(ol)}"

    print("✅ All OrderedList tests passed successfully!")

def testBinarySearchTree():
    # Test 1: Create tree and insert single node
    bst = BinarySearchTree()
    root = None
    bst.insert(root, 10 )
    assert bst.inorder(bst.getRoot()) == ["10"], f"❌ Test 1 Failed: {bst.inorder(bst.getRoot())}"

    # Test 2: Insert nodes to form BST
    bst = BinarySearchTree()
    root = None
    root = bst.insert(root, 10 )
    root = bst.insert(root, 5 )
    root = bst.insert(root, 15 )
    root = bst.insert(root, 3 )
    root = bst.insert(root, 7 )
    root = bst.insert(root, 12 )
    root = bst.insert(root, 18 )
    expected_inorder = ["3", "5", "7", "10", "12", "15", "18"]
    assert bst.inorder( bst.getRoot() ) == expected_inorder, f"❌ Test 2 Failed: {bst.inorder(bst.getRoot())}"

    # Test 3: Insert duplicate
    root = bst.insert(root, 10 )
    expected_inorder_with_duplicate = ["3", "5", "7", "10", "10", "12", "15", "18"]
    assert bst.inorder(bst.getRoot()) == expected_inorder_with_duplicate, f"❌ Test 3 Failed: {bst.inorder(bst.getRoot())}"

    # Test 4: String representation contains all nodes
    tree_str = str(bst)
    for val in expected_inorder_with_duplicate:
        assert val in tree_str, f"❌ Test 4 Failed: Value {val} not found in tree string"

    print("✅ All BinarySearchTree tests passed successfully!")

def testAVLTree():
    avl = AVLTree()
    root = None

    nodes = random.sample(range(1, 102), 101)
    for val in nodes:
        root = avl.insert(val, root)

    # Test 2: Check balance factor for root is within [-1, 1]
    def check_balance(node):
        if not node:
            return True
        left_height = node.getLeft().getHeight() if node.getLeft() else 0
        right_height = node.getRight().getHeight() if node.getRight() else 0
        balance = left_height - right_height
        if balance < -1 or balance > 1:
            return False
        return check_balance(node.getLeft()) and check_balance(node.getRight())

    assert check_balance(avl.getRoot()), "❌ Test 2 Failed: Tree is unbalanced"

    print("✅ All AVLTree tests passed successfully!")

testOrderedList()
testBinarySearchTree()
testAVLTree()