from Node import Node
import IDThree

class BinaryTree:

    def __init__(self):
        self.root:Node = None

    def insert_right(self, clave, key, data):
        node = Node(key, data)
        if(self.root.right == None or clave == None):
            self.root.right = node
        else:
            insert = self.search(clave)
            if(insert != None):
                insert.right = node
            else:
                return False
        
    def insert_left(self, clave, key, data):
        node = Node(key, data)
        if(self.root.left == None or clave == None):
            self.root.left = node
        else:
            insert = self.search(clave)
            if(insert != None):
                insert.left = node
            else:
                return False
       
    def search(self, key):
        nodo = Node.search_in_postOrder(self.root, key)
        return nodo

    def printTree(self):
        Node.print_postOrder(self.root)

    def test_path(self, path):
        node =  Node.path_by_dic(self.root, path)
        if node.key == -1:
            return -1
        else:
            variable, value = IDThree.obtener_entropia_minima(node.data)
            if IDThree.get_num_clase(node.data[variable]) > 1:
                if(path[variable] == 1):
                    return 1
                else:
                    return 0
            else:
                if node.data[variable][0][0] == 0:
                    return 0
                else:
                    return 1        