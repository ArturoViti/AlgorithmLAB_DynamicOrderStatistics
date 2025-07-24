from DataStructure.AVLTree import AVLTree
from DataStructure.Node.Node import Node
from DataStructure.OrderedList import OrderedList


if __name__ == '__main__':
    '''orderedList = OrderedList()
    orderedList.insert( Node(4) )
    orderedList.insert( Node(8) )
    orderedList.insert( Node(5) )
    orderedList.insert( Node(6) )
    print(orderedList)

    tree = BinarySearchTree(Node(15))
    tree.insert( Node(10) )
    tree.insert(Node(18))
    tree.insert(Node(4))
    tree.insert(Node(11))
    tree.insert(Node(16))
    tree.insert(Node(20))
    tree.insert(Node(13))
    print(tree)'''

    tree2 = AVLTree( Node(10))
    tree2.insert( Node(20) )
    tree2.insert( Node(30) )
    tree2.insert( Node(40) )
    tree2.insert( Node(50) )
    print(tree2)

    '''tree = AVLTestTree()
    tree.insert_value(10)
    tree.insert_value(20)
    tree.insert_value(30)
    tree.insert_value(40)
    tree.insert_value(50)

    print("Tree after insertion:")
    # In-order traversal to print the tree
    def inorder_traversal(root):
        if root:
            inorder_traversal(root.left)
            print(root.value),
            inorder_traversal(root.right)

    inorder_traversal(tree.root)
    print()'''