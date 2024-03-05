import IDThree
from BinaryTree import BinaryTree
from Node import Node
import data_stract
import random


def generate_binary_decition_tree(data):
    tree = BinaryTree()
    node = Node(random.randint(0,100), data)
    tree.root = node
    decition_tree(tree, tree.root.key, data)
    return tree

def decition_tree(tree, key, data):
    variable, value = IDThree.obtener_entropia_minima(data)
    if(value != 0 and IDThree.iterable_data(data)):
        dataL, dataR = IDThree.dividir_data(data, variable)
        keyL = generate_key(tree)
        keyR = generate_key(tree)
        tree.insert_left(key, keyL, dataL)
        tree.insert_right(key, keyR, dataR)
        decition_tree(tree, keyL, dataL)
        decition_tree(tree, keyR, dataR)
    else:
        return

def generate_key(tree):
    while(True):
        rand = random.randint(0,100)
        if(tree.search(rand) == None):
            return rand


