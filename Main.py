import decition_tree
import data_stract
import IDThree
import Node

print("------------------------------ID3------------------------------")
#Abrir la base de datos
file_path = "BD.xls"
train_sheet = "E"
test_sheet = "P"


#Extraemos la data de entrenamiento
data = data_stract.get_Data(file_path, train_sheet)
#print(data)
#Extraemos la data de prueba
dataP = data_stract.get_testData(file_path, test_sheet)
#print(dataP)

#Generamos el arbol de desicion
tree = decition_tree.generate_binary_decition_tree(data)
#Imprimimos el arbol de desicion
print("\nEl arbol de desicion en post-orden:")
#tree.printTree()

#Calculamos la eficacia con los datos de prueba
#result = []
#correcrto = 0
#for element in dataP:
#    test = tree.test_path(element[1])
#    result.append(test)
#    if element[0] == test:
#       correcrto+=1
#
#print("------------------------------\nLA EFICIENCIA ES: ", correcrto/len(dataP)*100, "%\nAciertos/total: ",  correcrto, "/", len(dataP))


questions = [
    "FEMENINO (SI) MASCULINO (NO)"
    "Tienes emisión de volumen excesivo de orina",
    "Tienes aumento anormal de sed",
    "Has tenido pérdida repentina de peso",
    "Has sentido debilidad",
    "Tienes aumento anormal en la necesidad de comer",
    "Tienes Flujo, ardor, picazón, irritación genital",
    "Tienes visión borrosa",
    "Tienes picazón en la piel, que hace que quieras rascarte",
    "Sufres de Irritabilidad",
    "Tienes cicatrización retardada",
    "Tienes disminución de la fuerza, debilidad muscular.",
    "Tienes dolor en las articulaciones",
    "Tienes pérdida anormal del cabello",
    "Tienes sobrepeso",
    "-50 (SI) +=50 (NO)"
]

#tree.addQ(questions)
tree.printTree()

ls = [1,1,1]
node = tree.root
while node.left != None:
    index, dat = IDThree.obtener_entropia_minima(node.data)
    print(questions[index-1])
    answ = int(input())
    
    if answ == 1:
        node = node.left
    else:
        node = node.right
    
index, dat = IDThree.obtener_entropia_minima(node.data)
print(questions[index-1])
clas = Node.Node.getClass(node.data[index])

answ = int(input())

if clas == "GREEN":
    print("Test positive")
elif clas == "RED":
    print("Test negative")
elif clas == "BLUE":
    if answ ==1:
        print("Test positive")
    else:
        print("Test negative")
elif clas == "VIOLET":
    if answ ==0:
        print("Test positive")
    else:
        print("Test negative")
else:
   print("EL SISTEMA NO PUEDE CLASIFICAR ESTA ENTRADA")