from BinaryNode import BinaryNode


class BinaryTree:

    def __init__(self):
        self.root:BinaryNode = None
    
    #
    # Search Methods
    #

    def search(nodo:BinaryNode,key):
        return __class__._search(key, nodo)

    @staticmethod
    def _search(key, node:BinaryNode) -> BinaryNode:
        if node is None:
            return None
        if node.key > key:
            return BinaryTree._search(key, node.Left)
        if node.key < key:
            return BinaryTree._search(key, node.Right)
        # Case node.key == key
        return node

    def search_min(self) ->BinaryNode:
        return BinaryTree._search_min(self.root)

    @staticmethod
    def _search_min(node:BinaryNode)->BinaryNode:
        if node is None:
            return None
        if node.Left is None:
            return node.data
        return __class__._search_min(node.Left)

    def search_max(self)->BinaryNode:
        node = self.root
        if node is not None:
            while node.Right is not None:
                node = node.right
            return node.data
        else:
            return None
        
        
    #
    # Calculate the tree
    #
    
    # Size of tree with that node as root
    def size(self,key)->int:
        if self.root is None: return 'Arbol Vacio'
        if key is None : key = self.root
        else: key = __class__.search(self.root,key)
        try:
            return __class__._size(key)
        except Exception:
            print('Se dio un dato mal')
            return 
            
    @staticmethod
    def _size(root:BinaryNode) -> int:
        if root is None:
            return 0
        else:
            return 1 + BinaryTree._size(root.Left) + BinaryTree._size(root.Right)

    # Height: The largest number of edges from the root to the most distant leaf node.
    def height(self,key:BinaryNode=None)->int:
        if self.root is None: return 'Arbol Vacio'
        if key is None: key = self.root
        else: key = __class__.search(self.root,key)
        try:
            return __class__._height(key)
        except Exception:
            print('Se dio un dato mal')
            return 
    @staticmethod
    def _height(root:BinaryNode):
        # This is a ternary operator in Python (0 if True, 1 + height(right) if False)
        right_height = 0 if root.Right is None else 1 + BinaryTree._height(root.Right)
        left_height = 0 if root.Left is None else 1 + BinaryTree._height(root.Left)

        # Returns the largest value
        return right_height if right_height >= left_height else left_height

    # Deep: from the root, how many levels you need to reach
    def deep(self,key)->int:
        if self.root is None: return 'Arbol Vacio'
        if key is None: key = self.root.key
        try:
            return __class__._deep(self.root,key,1)
        except Exception:
            print('Se dio un dato mal')
            return 
    @staticmethod
    def _deep(root:BinaryNode,key,level):
        if root is None:
            return -1
        
        if root.key== key:
            return level
        
        deepLeft = __class__._deep(root.Left,key,level+1)
        if deepLeft != -1: return deepLeft
        
        deepRight = __class__._deep(root.Right,key,level+1)
        return deepRight

    @staticmethod
    def findDad(nodo:BinaryNode, data:BinaryNode) -> BinaryNode:
        if nodo is None or nodo == data:
            return
        
        if nodo.Left == data: return nodo
        if nodo.Right == data: return nodo
        
        leftdad = __class__.findDad(nodo.Left,data)
        if leftdad is not None:
            return leftdad
        
        rightdad = __class__.findDad(nodo.Right,data) 
        return rightdad
        
    def brother(self,key):
        if self.root is None: return 'Arbol Vacio'
        if key is None: key = self.root
        else: key = __class__.search(self.root,key)
        try:
            return __class__._getbrother(self.root,key)
        except Exception:
            print('Se dio un dato mal')
            return 
    @staticmethod    
    def _getbrother(nodo:BinaryNode,data):
        dad = __class__.findDad(nodo,data)
        if dad is None: return None # si el papa no existe
        try:
            if dad.Left.key == data.key: return dad.Right.data
            else: return dad.Left.data
        except Exception: return False

    def anubis(self,key):
        if self.root is None: return 'Arbol Vacio'
        if key is None: key = self.root
        else: key = __class__.search(self.root,key)
        __class__._anubisNodes(self.root,key)
        return __class__._anubis(self.root, key.data, [])
    
    
    @staticmethod
    def _anubisNodes(root:BinaryNode,key:BinaryNode):
        if root == key:
            print(f'{root.key}')
            return
        ansestor = __class__.findDad(root,key)
        print(f'{ansestor.key} - ')
        __class__._anubisNodes(root,ansestor)
        
        
        
    def _anubis(nodo:BinaryNode,data,anubis):
        if nodo is None:
            return []
        stack = [(nodo, [])]
        while stack:
            actual, anubis = stack.pop()
            if actual == nodo:
                return anubis
            if actual.Left:
                stack.append((actual.Left, anubis + [actual.data]))
            if actual.Right:
                stack.append((actual.Right, anubis + [actual.data]))
        return []
        

    #
    # Insertion Methods
    #
    def insert_KeyAsData(self, data): # sabiendo que la variable key va a ser igual al data, tomamos en cuenta eso
        self.root = BinaryTree.__insert(data,data,self.root)
        
    def insert(self, data, key): # permite poner data repetida dando una key diferente
        self.root = BinaryTree.__insert(data, key, self.root)
    @staticmethod
    def __insert(data, key, node:BinaryNode):
        if node is None:
            node = BinaryNode(data, key)
        elif key < node.key:
            node.Left = BinaryTree.__insert(data, key, node.Left)
        elif key > node.key:
            node.Right = BinaryTree.__insert(data, key, node.Right)
        else:
            print("Duplicado. Error al insertar")
        return node

    #
    # Delete methods
    #

    def delete_min(self):
        self.root = __class__._delete_min(self.root)

    @staticmethod
    def _delete_min(node:BinaryNode):
        if node is None:
            print("Árbol vacío. Error al borrar")
        elif node.Left is not None:
            node.Left = __class__._delete_min(node.Left)
        else:
            node = node.Right
        return node

    def delete(self, key):
        if key is None: key = self.root.key
        self.root = __class__._delete(key, self.root)

    @staticmethod
    def _delete(key, node:BinaryNode):
        if node is None:
            print("Árbol vacío. Error al borrar")
        elif key < node.key:
            node.Left = BinaryTree._delete(key, node.Left)
        elif key > node.key:
            node.Right = BinaryTree._delete(key, node.Right)
        elif node.Left is not None and node.Right is not None:
            tempNodo = __class__.search(node,node.Right.key)
            node.key = tempNodo.key
            node.data = tempNodo.data
            node.Right = __class__._delete_min(node.Right)
        else: node = node.Left if node.Left is not None else node.Right
        return node

    # Print tree traverse

    def preorder(self):
        if self.root is None: return 'Arbol vacio'
        self.root.print_preorder()
        return '\n'

    def inorder(self):
        if self.root is None: return 'Arbol vacio'
        self.root.print_inorder()
        return '\n'

    def postorder(self):
        if self.root is None: return 'Arbol vacio'
        self.root.print_postorder()
        return '\n'

    def levels(self):
        if self.root is None: return 'Arbol vacio'
        BinaryNode.travers_by_levels(self.root)
        return '\n'

    def getSibiling(self, key):
        if self.root is None: return 'Arbol Vacio'
        if not (key == self.root.key):
            aux = []
            BinaryTree._getFather(key, self.root, aux)
            if not aux[0] is None:
                if BinaryTree._comleteLeaves(aux[0]):
                    if aux[0].Left.key == key:
                        return aux[0].Right
                    return aux[0].Left 
            else:
                return None
        else:
            return None
    
    @staticmethod
    def _getFather(key, node, aux):
        if node is None:
            return None
        if(BinaryTree._isInstantChild(key,node)):
            aux.append(node)
        else:
            if key < node.key:
                BinaryTree._getFather(key, node.Left, aux)
            if key > node.key:
                BinaryTree._getFather(key, node.Right, aux)

    @staticmethod
    def _isInstantChild(key, node):
        if not (node.Left is None):
            if node.Left.key == key:
                return True
        if not (node.Right is None):
            if node.Right.key == key:
                return True
        return False
    
    @staticmethod
    def _comleteLeaves(node):
        if node.Left is None:
            return False
        if node.Right is None:
            return False
        return True

    def descendientes(self, key):
        descen = []
        if self.root is None: return descen
        if key is None: key = self.root.key
        node = self.searchNode(key)
        #print(node)
        if not node is None:
            BinaryTree._descendientes(node, descen)
            descen.pop(0)
            return descen
        else:
            return None
    
    def _descendientes(node, lista):
        if node is None:
            return None
        else:
            lista.append(node)
            if(not node.Left is None):
                BinaryTree._descendientes(node.Left, lista)
            if(not node.Right is None):
                BinaryTree._descendientes(node.Right, lista)

    def searchNode(self, key):
        return BinaryTree._searchNode(key, self.root)

    @staticmethod
    def _searchNode(key, node):
        if node is None:
            return None
        if node.key > key:
            return BinaryTree._searchNode(key, node.Left)
        if node.key < key:
            return BinaryTree._searchNode(key, node.Right)
        # Case node.key == key
        return node

    def isABC(self):
        if self.root is None: return 'Arbol Vacio'
        aux = []
        BinaryTree._isABC(self.root, aux)
        return not (1 in aux)
    
    @staticmethod
    def _isABC(node, abc):
        if node is None:
            return None
        else:
            if (node.Left is None and not node.Right is None) or (not node.Left is None and node.Right is None):
                abc.append(1)
            BinaryTree._isABC(node.Left, abc)
            BinaryTree._isABC(node.Right, abc)

    def getAncestros(self, key):
        ancestros = []
        if self.root is None: return ancestros
        if key is None: key = self.root.key
        BinaryTree._getAncestros(self.root, key, ancestros)
        return ancestros
    
    @staticmethod
    def _getAncestros(node, key, listaA):
        if node is None:
            return None
        if node.key > key:
            BinaryTree._getAncestros(node.Left, key, listaA)
        if node.key < key:
            BinaryTree._getAncestros(node.Right, key, listaA)
        if node.key == key:
            return True
        listaA.append(node)
        
    


'''
    
    def asignLeft(self, data):
        self.Left = __class__.__init__(data)
    def asignRight(self,data):
        self.Right = __class__.__init__(data)
    def asignAtNode(self,dataLeft,dataRight):
        self.Left = BinaryNode(dataLeft)
        self.Right = BinaryNode(dataRight)
        
          
    def recursiveInsert(nodo:BinaryNode,data):
        if nodo is None:
            nodo = BinaryNode(data)
        if data < nodo.data:
            nodo.Left = __class__.recursiveInsert(nodo.Left,data)
        else:
            nodo.Right = __class__.recursiveInsert(nodo.Right,data)
        return nodo
    
    def insertData(self,data):
            self.iniNodo = __class__.recursiveInsert(self.iniNodo,data)
    
    def showPost(self):
        string = str(self.data)
        if (self.Left != None):
            string = string+' - ' + self.Left.showPre()
        if (self.Right != None):
            string = string+' - ' + self.Right.showPre()
        return string
    
    def clone(self):    
        root = __class__(self.data)
        if self.Left != None :
            root.Left = self.Left.clone()
        if self.Right != None:
            root.Right = self.Right.clone()
        return root

    def size(nodo) -> int:
        if (nodo is None):
            return 0
        else:
            return 1+__class__.size(nodo.Left) + __class__.size(nodo.Right)
        
    def sizeTree(self) -> int:
        return __class__.size(self.iniNodo)
    
    def height(nodo):
        if nodo is None:
            return -1
        
        heightLeft = __class__.height(nodo.Left)
        heightRight = __class__.height(nodo.Right)
        
        if heightLeft>heightRight:
            return 1+heightLeft
        else:
            return 1+heightRight

    def deep(node:BinaryNode,data:int,nivel:int) -> int:
        if node is None:
            return -1
        
        if node.data == data:
            return nivel
        
        deepLeft = __class__.deep(node.Left,data,nivel+1)
        deepRight = __class__.deep(node.Right,data,nivel+1)
        
        if deepLeft != -1: return deepLeft
        return deepRight
    
    def deepIni(self,data):
        return __class__.deep(self.iniNodo,data,0) # 0 es el nivel inicial
        
    def findDad(nodo:BinaryNode, data) -> BinaryNode:
        if nodo is None or nodo.data == data:
            return
        if nodo.Left.data == data or nodo.Right.data == data:
            return nodo
        leftdad = __class__.findDad(nodo.Left,data)
        rightdad = __class__.findDad(nodo.Right,data)
        if leftdad is not None:return leftdad
        else: return rightdad
        
    def getbrother(nodo,data):
        dad = __class__.findDad(nodo,data)
        if dad is None: return None # si el papa no existe
        if dad.Left.data == nodo: return dad.Right.data
        else: return dad.Left.data
        
        
    def get_anubis(nodo:BinaryNode,data,anubis):
        if nodo is None:
            return []
        stack = [(nodo, [])]
        while stack:
            actual, anubis = stack.pop()
            if actual == nodo:
                return anubis
            if actual.Left:
                stack.append((actual.Left, anubis + [actual.data]))
            if actual.Right:
                stack.append((actual.Right, anubis + [actual.data]))
        return []

    def get_desanubis(nodo) -> list:
        if nodo is None:
            return []

        descendientes = []
        stack = [nodo]

        while stack:
            actual = stack.pop()
            if actual.Left:
                stack.append(actual.Left)
                descendientes.append(actual.Left.data)
            if actual.Right:
                stack.append(actual.Right)
                descendientes.append(actual.Right.data)

        return descendientes

    def preOrden(nodo:BinaryNode):
        if nodo is None:
            return
        print(nodo.data)
        __class__.preOrden(nodo.Left)
        __class__.preOrden(nodo.Right)
        
    def inOrden(nodo:BinaryNode):
        if nodo is None:
            return
        __class__.inOrden(nodo.Left)
        print(nodo.data)
        __class__.inOrden(nodo.Right)
        
    def postOrden(nodo:BinaryNode):
        if nodo is None:
            return
        __class__.postOrden(nodo.Left)
        __class__.postOrden(nodo.Right)
        print(nodo.data)

    def findSucesorInOrden(nodo:BinaryNode):
        nodoActual = nodo.Right
        while nodoActual.Left:
            nodoActual = nodoActual.Left
        return nodoActual

    def deleteNode(nodo:BinaryNode,dato):
        if nodo is None:
            return nodo
        if dato < nodo.data:
            nodo.Left = __class__.deleteNode(nodo.Left,dato)
        elif dato> nodo.data:
            nodo.Right = __class__.deleteNode(nodo.Right,dato)
        else:
            if nodo.Left is None:
                return nodo.Right
            elif nodo.Right is None:
                return nodo.Left
            else:
                sucesor = __class__.findSucesorInOrden(nodo)
                nodo.data = sucesor.data
                nodo.Right = __class__.deleteNode(nodo.Right,sucesor.data)
        return nodo


if __name__ == '__main__':
    mainNodo = BinaryNode(3)
    mainNodo.asignAtNode(1,2)
    
    print(mainNodo.show(),'\n======================\n',mainNodo.showPre())
    
    print(mainNodo.size())
    
'''
