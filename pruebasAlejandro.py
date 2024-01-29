from BinaryTree import BinaryTree

arbol = BinaryTree()

arbol.insert(5, 5)
arbol.insert(6, 6)
arbol.insert(7, 7)
arbol.insert(2, 2)
arbol.insert(4, 4)
arbol.insert(10, 10)
arbol.insert(22, 22)
arbol.insert(1, 1)
arbol.insert(3, 3)
arbol.insert(8, 8)

anses = []
anses = arbol.getAncestros(3)
for element in anses:
    if not element is None:
        print(element.key)

print(anses)