import IDThree
import data_stract

file_path = "BASE_ORIGINAL.xls"
dataY, dataO = data_stract.get_variables(file_path)


print(IDThree.obtener_entropia_minima(dataO))

dataB, dataC = IDThree.dividir_data(dataO, 2)

print(IDThree.obtener_entropia_minima(dataB))
print(IDThree.obtener_entropia_minima(dataC))

dataD, dataE = IDThree.dividir_data(dataB, 15)
print("hoLA",IDThree.obtener_entropia_minima(dataD))
print(IDThree.obtener_entropia_minima(dataE))

dataF, dataG = IDThree.dividir_data(dataC, 1)
print(IDThree.obtener_entropia_minima(dataF))
print(IDThree.obtener_entropia_minima(dataG))

dataH, dataI = IDThree.dividir_data(dataD, 3)
print("H",IDThree.obtener_entropia_minima(dataH))
print(IDThree.obtener_entropia_minima(dataI))

dataJ, dataK = IDThree.dividir_data(dataF, 13)
print(IDThree.obtener_entropia_minima(dataJ))
print(IDThree.obtener_entropia_minima(dataK))

dataL ,dataM = IDThree.dividir_data(dataG, 3)
print(IDThree.obtener_entropia_minima(dataL))
print(IDThree.obtener_entropia_minima(dataM))

dataN ,dataO =IDThree.dividir_data(dataK, 8)
print(IDThree.obtener_entropia_minima(dataN))
print(IDThree.obtener_entropia_minima(dataO))

dataP ,dataQ = IDThree.dividir_data(dataL, 12)
print(IDThree.obtener_entropia_minima(dataP))
print(IDThree.obtener_entropia_minima(dataQ))

dataR, dataS = IDThree.dividir_data(dataM, 11)
print(IDThree.obtener_entropia_minima(dataR))
print(IDThree.obtener_entropia_minima(dataS))

dataT, dataU = IDThree.dividir_data(dataO, 15)
print(IDThree.obtener_entropia_minima(dataT))
print(IDThree.obtener_entropia_minima(dataU))

dataV, dataW = IDThree.dividir_data(dataR, 14)
print(IDThree.obtener_entropia_minima(dataV))
print(IDThree.obtener_entropia_minima(dataW))

dataX, dataY = IDThree.dividir_data(dataU, 10)
print(IDThree.obtener_entropia_minima(dataX))
print(IDThree.obtener_entropia_minima(dataY))

dataZ, dataA1 = IDThree.dividir_data(dataV, 9)

print(IDThree.obtener_entropia_minima(dataZ))
print(IDThree.obtener_entropia_minima(dataA1))

dataB1, dataC1 = IDThree.dividir_data(dataY, 5)
print(IDThree.obtener_entropia_minima(dataB1))
print(IDThree.obtener_entropia_minima(dataC1))

dataD1, dataE1 = IDThree.dividir_data(dataC1, 4)
print(IDThree.obtener_entropia_minima(dataD1))
print(IDThree.obtener_entropia_minima(dataE1))

dataF1, dataG1 = IDThree.dividir_data(dataE1, 6)
print(IDThree.obtener_entropia_minima(dataF1))
print(IDThree.obtener_entropia_minima(dataG1))

dataH1, dataI1 = IDThree.dividir_data(dataG1, 3)
print(dataH1)
print(IDThree.iterable_data(dataH1))
#print("Hola: ",IDThree.obtener_entropia_minima(dataH1))
#print(IDThree.obtener_entropia_minima(dataI1))














