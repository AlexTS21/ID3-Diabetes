import os
from BinaryTree import BinaryTree

def hitenter(): # permite pulsar enter para continuar
    try: input()
    except Exception: pass

def intInput() -> int:
    # permite abrir el archivo
    while True:
        try:
            vInput = int(input('Ingresa el numero: '))
            break
        except ValueError: print('Error: Se inserto un dato no valido\n')
    return vInput

def read_file(path:str) -> BinaryTree:
    #print(path)
    while True: # solo aceptara un archivo legal
        try:
            vInput = str(input('Ingresa archivo a buscar: ')) 
            if '.txt' in vInput:pass # el input puede ser "1.txt" o "1"
            else: vInput=vInput+'.txt'
            break
        except ValueError: print('Error: Se inserto un dato no valido\n')
    
    name = path+vInput

    tree = BinaryTree()
    try:
        with open(name) as file:
            content = file.read() # obtenemos archivos
            values = content.split(", ") # dividimos

            for i in values:
                # print(i)
                # Al insertar hay que pasar: Dato (data) y clave (key)
                tree.insert_KeyAsData(int(i))
        print('\nSe ha importado correctamente el Arbol')
    except FileNotFoundError: print(f'\nNo existe el archivo: {vInput}')
    except Exception: print(f'Ni idea en que fallo, haha\n')
    
    return tree

def menumain():
    print('Arbol Binarios de Busqueda')
    options = ['Importar Arbol', #1
               'Insertar al Arbol', #2
               'Borrar al Arbol', #3
               'Imprimir Arbol', #4
               'Calcular Arbol', #5
               'Determinar ABC'] #6
    for idx,opt in enumerate(options): print(f'{(idx+1):>2}- {opt}')
    print(f'{0:>2}- exit')
    
def menuExport(tree:BinaryTree):
    vInput=-1
    print('Arbol Binarios de Busqueda - Visualizar')
    options = ['Recorrido en PreOrden',
               'Recorrido en InOrden',
               'Recorrido en PostOrden',
               'Recorrido en Niveles']
    while vInput != 0:
        for idx,opt in enumerate(options): print(f'{(idx+1):>2}- {opt}')
        print(f'{0:>2}- exit')
        vInput = intInput()
        if vInput == 1: print(tree.preorder())
        elif vInput == 2: print(tree.inorder())
        elif vInput == 3: print(tree.postorder())
        elif vInput == 4: print(tree.levels())
        elif vInput == 0: return
        else: print('Se dio una opcion no valida\n')
        hitenter()
def inputKey(): # permite poner un nodo
    while True:
        try:
            vInput = input('Si desea buscar desde un nodo ingreselo\n(si deja vacio, la busqueda es desde la raiz): ')
            if vInput == '' : return None
            vInput= int(vInput)
            break
        except ValueError: print('Error: Se inserto un dato no valido\n')
    return vInput 

def menuCalculate(tree:BinaryTree):
    vInput=-1
    print('Arbol Binarios de Busqueda - Visualizar')
    options = ['Calcular Profundidad', #1
               'Calcular Altura', #2
               'Calcular Tamano', #3
               'Obtener Hermanos', #4
               'Obtener Ancestros', #5
               'Obtener Descendientes' #6
               ]
    while vInput != 0:
        for idx,opt in enumerate(options): print(f'{(idx+1):>2}- {opt}')
        print(f'{0:>2}- exit')
        vInput = intInput()
        
        if   vInput == 1: print(f'La profundidad del arbol es de: {tree.deep(inputKey())}\n')
        elif vInput == 2: print(f'La Altura del arbol es de: {tree.height(inputKey())}\n')
        elif vInput == 3: print(f'El tamano del arbol es de: {tree.size(inputKey())}\n')
        elif vInput == 4:
            getB = tree.brother(inputKey())
            if getB is False: print('Este nodo no tiene hermano') 
            else: print(f'El Hermano del nodo es de: {getB}\n')
        elif vInput == 5:
            print(f'El Ancestro del nodo es el: \n')
            for num,idx in enumerate(tree.getAncestros(inputKey())):
                if num%10 == 0 and num != 0: print('\n')
                if not idx is None: print(f'{idx.key:<7}', end='-')
            print('\n')
        
        elif vInput == 6: 
            print(f'Los Descendientes del nodo son: \n')
            for num,idx in enumerate(tree.descendientes(inputKey())):
                if num%10 == 0 and num != 0: print('\n')
                if not idx is None: print(f'{idx.key:<7}', end='-')
            print('\n')
                
        elif vInput == 0: print('Saliendo del submenu...') 
        
        else: print('Se dio una opcion no valida\n')
def isABC(tree:BinaryTree):
    if tree.isABC():
          print('El arbol que se tiene es un Arbol Binario Completo')
    else: print('El arbol que se tiene NO es un arbol Binario Completo :c')

def main():
    pydir = str(os.path.dirname(os.path.abspath(__file__))) + '\\arbolestxt\\'
    #print(pydir)
    arbol = BinaryTree()
    
    vInput=-1
        
    while vInput != 0:
        menumain()
        vInput = intInput()
        if vInput == 1: arbol = read_file(pydir)
        elif vInput == 2:
            arbol.insert_KeyAsData(intInput())
            print('Se ha ananido :)')
        elif vInput == 3:
            arbol.delete(intInput())
            print('Se ha borrado :)')
        elif vInput == 4: menuExport(arbol)
        elif vInput == 5: menuCalculate(arbol)
        elif vInput == 6:
            isABC(arbol)
            hitenter()
        elif vInput == 0: break 
        else: print('Se dio una opcion no valida\n')
    '''print('Desea guardar el arbol?: [1: si][2: no]')
    saveIn = intInput()
    if saveIn == 1:
        with open(pydir)'''
    print('Cerrando Programa...')

if __name__ == '__main__':
    main()