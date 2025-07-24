from DataStructure.Node.AVLNode import AVLNode
from DataStructure.Node.ListNode import ListNode
from DataStructure.Node.Node import Node
from DataStructure.Node.TreeNode import TreeNode


def testNode():
    # Test creation and getValue
    n = Node(10)
    assert n.getValue() == 10, "❌ Initial value is incorrect"

    # Test setValue
    n.setValue(20)
    assert n.getValue() == 20, "❌ setValue did not update the value"

    # Test __str__
    assert str(n) == "Node Value:20", "__str__ does not return the correct string"

    # Test comparisons
    n1 = Node(5)
    n2 = Node(10)
    n3 = Node(5)

    assert n1 < n2, "❌ Comparison < failed"
    assert n2 > n1, "❌ Comparison > failed"
    assert n1 == n3, "❌ Comparison == failed"
    assert not (n1 == n2), "❌ Inequality test failed"

    print("✅ Node tests passed!")

def testListNode():
    ln1 = ListNode(1)
    ln2 = ListNode(2)

    # Test that next is initially None
    assert ln1.getNext() is None, "❌ Initial next node should be None"

    # Test setting and getting next node
    ln1.setNext(ln2)
    assert ln1.getNext() == ln2, "❌ getNext did not return the correct next node"
    assert ln1.getNext().getValue() == 2, "❌ Next node does not have expected value"

    # Test updating next node
    ln3 = ListNode(3)
    ln1.setNext(ln3)
    assert ln1.getNext() == ln3, "❌ Next node was not updated correctly"

    print("✅ ListNode tests passed!")

def testTreeNode():
    tn1 = TreeNode(1)
    tn_left = TreeNode(2)
    tn_right = TreeNode(3)

    # Initially, left and right should be None
    assert tn1.getLeft() is None, "❌ Initial left node should be None"
    assert tn1.getRight() is None, "❌ Initial right node should be None"

    # Set left and right nodes
    tn1.setLeft(tn_left)
    tn1.setRight(tn_right)

    # Check left and right nodes
    assert tn1.getLeft() == tn_left, "❌ getLeft did not return the correct node"
    assert tn1.getRight() == tn_right, "❌ getRight did not return the correct node"
    assert tn1.getLeft().getValue() == 2, "❌ Left child value is incorrect"
    assert tn1.getRight().getValue() == 3, "❌ Right child value is incorrect"

    # Update left and right nodes
    new_left = TreeNode(4)
    tn1.setLeft(new_left)
    assert tn1.getLeft() == new_left, "❌ Left node was not updated correctly"

    print("✅ TreeNode tests passed!")

def testAVLNode():
    avl = AVLNode(10)
    left = AVLNode(5)
    right = AVLNode(15)

    # Initial height and size
    assert avl.getHeight() == 1, "❌ Initial height should be 1"
    assert avl.getSize() == 1, "❌ Initial size should be 1"

    # Set and get height
    avl.setHeight(3)
    assert avl.getHeight() == 3, "❌ Height not updated correctly"

    # Set and get size
    avl.setSize(7)
    assert avl.getSize() == 7, "❌ Size not updated correctly"

    # Initially, left and right should be None
    assert avl.getLeft() is None, "❌ Initial left should be None"
    assert avl.getRight() is None, "❌ Initial right should be None"

    # Set and get left/right nodes
    avl.setLeft(left)
    avl.setRight(right)

    assert avl.getLeft() == left, "❌ Left node not set correctly"
    assert avl.getRight() == right, "❌ Right node not set correctly"
    assert avl.getLeft().getValue() == 5, "❌ Left node value incorrect"
    assert avl.getRight().getValue() == 15, "❌ Right node value incorrect"

    print("✅ AVLNode tests passed!")


# Run the tests
testNode()
testListNode()
testTreeNode()
testAVLNode()
