import decition_tree
import data_stract

print("------------------------------ID3------------------------------")
#Abrir la base de datos
file_path = "BD.xls"#input("Nombre de la base de datos (archivo xls): ") + ".xls"
train_sheet = "E" #input("Hoja de entrenamiento: ") #E
test_sheet = "P" #input("Hoja de prueba: ") #P


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
tree.printTree()

#Calculamos la eficacia con los datos de prueba
result = []
correcrto = 0
for element in dataP:
    test = tree.test_path(element[1])
    result.append(test)
    if element[0] == test:
       correcrto+=1

print("------------------------------\nLA EFICIENCIA ES: ", correcrto/len(dataP)*100, "%\nAciertos/total: ",  correcrto, "/", len(dataP))
input("Precione una tecla para terminar el programa")