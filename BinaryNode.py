from ListaSimpleLigada import Lista as Cola


class BinaryNode:
    def __init__(self, data, key):
        self.data = data
        self.Left: BinaryNode = None
        self.Right: BinaryNode = None
        self.key = key

    def clone(self):
        root = BinaryNode(self.data, self.key)
        if self.Left is not None:
            root.Left = self.Left.clone()
        if self.Right is not None:
            root.Right = self.Right.clone()
        return root

    #
    # Tree Traversals (Inorder, Preorder and Postorder)
    #

    # Preorder
    def print_preorder(self):
        print(self.data, end=" ")
        if self.Left is not None:
            self.Left.print_preorder()
        if self.Right is not None:
            self.Right.print_preorder()

    # Inorder
    def print_inorder(self):
        if self.Left is not None:
            self.Left.print_inorder()
        print(self.data, end=" ")
        if self.Right is not None:
            self.Right.print_inorder()

    # Postorder
    def print_postorder(self):
        if self.Left is not None:
            self.Left.print_postorder()
        if self.Right is not None:
            self.Right.print_postorder()
        print(self.data, end=" ")

    # Level Order Binary Tree Traversal
    @staticmethod
    def travers_by_levels(node):
        queue = Cola()
        queue.push((node, 0))

        while not queue.esta_vacia():
            element, level = queue.pop()

            #print("dato: ", element.data, " nivel: ", level)
            print(f'Dato: {element.data :<6} Nivel: {level :<6}')
            if element.Left is not None:
                queue.push((element.Left, level + 1))
            if element.Right is not None:
                queue.push((element.Right, level + 1))
    def travers_by_levels_grafic(node):
        queue = Cola()
        queue.push((node, 0))

        while not queue.esta_vacia():
            element, level = queue.pop()

            #print("dato: ", element.data, " nivel: ", level)
            print(f'Dato: {element.data :<6} Nivel: {level :<6}')
            if element.Left is not None:
                queue.push((element.Left, level + 1))
            if element.Right is not None:
                queue.push((element.Right, level + 1))



