import IDThree
class Node:
    def __init__(self, clave, data):
        self.data = data
        self.key = clave
        self.right = None
        self.left = None

    @staticmethod
    def search_in_postOrder(node, clave):
        if node is None:
            return None
        if node.key == clave:
            return node
        # Traverse left and then right
        left_result = node.search_in_postOrder(node.left, clave)
        if left_result:
            return left_result
        return node.search_in_postOrder(node.right, clave)
            

    @staticmethod
    def print_postOrder(node):
        if(node.right != None):
            node.print_postOrder(node.right)
        if(node.left != None):
            node.print_postOrder(node.left)
        
        index, dat = IDThree.obtener_entropia_minima(node.data)
        if(node.left ==None):
            if(node.key != -1):
                print("(", index, ",", dat,") \t\t\t", Node.getClass(node.data[index]))
            else:
                print("(", index, ", - ) \t\t\tNO RESULT")
        else:
            print("(", index, ",", dat,") ")
    
    @staticmethod
    def getClass(tup):
        cals = tup[0][0]
        flag = 0
        i=1
        for element in tup:
            if(i < len(tup)):
                if(element[0] != tup[i][0]):
                    flag = 1
            i+=1
        if(flag == 0):
            if(cals == 1):
                return "GREEN"
            else:
                return "RED"
        else:
            if(tup[0][0] == tup[0][1]):
                return "BLUE"
        return "VIOLET"



# La clase node es un nodo que tiene dos enlaces, uno para la dereha y otro para la izuierda
        
    @staticmethod
    def path_by_dic(node, path):
        variable, value = IDThree.obtener_entropia_minima(node.data)
        if node is None:
            return None
        if node.right is None and node.left is None:
            return node
        #Traverse
        if(path[variable] == 1):
            return Node.path_by_dic(node.left, path)
        return Node.path_by_dic(node.right, path)
        