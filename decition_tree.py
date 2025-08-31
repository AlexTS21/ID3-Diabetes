from .IDThree import obtener_entropia_minima, iterable_data, dividir_data
from .BinaryTree import BinaryTree
from .Node import Node
from random import randint

def generate_binary_decition_tree(data):
    tree = BinaryTree()
    node = Node(randint(0,100), data)
    tree.root = node
    decition_tree(tree, tree.root.key, data)
    return tree

def decition_tree(tree, key, data):
    variable, value = obtener_entropia_minima(data)
    if(value != 0 and iterable_data(data)):
        dataL, dataR = dividir_data(data, variable)
        keyL = generate_key(tree)
        keyR = generate_key(tree)
        tree.insert_left(key, keyL, dataL)
        tree.insert_right(key, keyR, dataR)
        decition_tree(tree, keyL, dataL)
        decition_tree(tree, keyR, dataR)
    elif(not iterable_data(data) and value!=0):
        node = tree.search(key)
        node.key = -1
    else:
        return

def generate_key(tree):
    while(True):
        rand = randint(0,100)
        if(tree.search(rand) == None):
            return rand