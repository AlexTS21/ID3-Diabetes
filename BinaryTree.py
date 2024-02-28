from Node import Node


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
    
        
            



    
