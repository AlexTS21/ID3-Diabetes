import IDThree
import Entropia
import BinaryTree
import data_stract


data = data_stract.get_variables("BASE_ORIGINAL.xls")

def decision_tree(data):
    tree = BinaryTree.BinaryTree()
    tree.

    
    return tree

def d_t_r(tree, data):
    entropia = IDThree.obtener_entropia_minima(data)
    if(entropia != 0):
        dataI, dataD = IDThree.dividir_data(entropia)

    else:
        return