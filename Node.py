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
        print(node.data)
# La clase node es un nodo que tiene dos enlaces, uno para la dereha y otro para la izuierda


