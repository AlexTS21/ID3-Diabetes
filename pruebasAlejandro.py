import IDThree
import data_stract

file_path = "BASE_ORIGINAL.xls"
dataY, dataO = data_stract.get_variables(file_path)


print(IDThree.obtener_entropia_minima(dataY))

dataB, dataC = IDThree.dividir_data(dataY, 3)
print(IDThree.obtener_entropia_minima(dataB))

dataD, dataE = IDThree.dividir_data(dataB, 2)
print(IDThree.obtener_entropia_minima(dataE))
