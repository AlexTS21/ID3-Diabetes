import IDThree
import data_stract
import decition_tree


dataY, dataO =data_stract.get_variables("DATA_PRUEBA.xls", "APR")
dataYP, dataOP = data_stract.data_stact_prueba("DATA_PRUEBA.xls", "PRB")

tree = decition_tree.generate_binary_decition_tree(dataY)
tree.printTree()
count = 0
total=0
value = None
for element in dataYP:
    value = tree.test_path(element[1])
    if value != -1:
        print(element[0], value)
        if(element[0] == value):
            count+=1
    total+=1

print(count/total)
print(len(dataYP), "total ", count)


tree2 = decition_tree.generate_binary_decition_tree(dataO)
count = 0
total=0
value = None
for element in dataOP:
    value = tree2.test_path(element[1])
    if value != -1:
        if(element[0] == value):
            count+=1
    total+=1

print(count/total)
print(len(dataYP), "total ", count)