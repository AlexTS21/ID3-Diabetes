from BinaryTree import BinaryTree
from Node import Node

arbol = BinaryTree()

arbol.root = Node(1, 1)

arbol.insert_right(1, 2, 2)
arbol.insert_left(1,3,3)

arbol.insert_left(2,4,4)
arbol.insert_right(2,4,4)


arbol.printTree()