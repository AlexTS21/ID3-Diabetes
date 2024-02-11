import IDThree
import data_stract

file_path = "BASE_ORIGINAL.xls"
dataY, dataO = data_stract.get_variables(file_path)

#JOVENES---------------------------------------------------------------------
#Primera Iteracion
print(IDThree.obtener_entropia_minima(dataY))

#Primera divicion----------------------
dataYB, dataYC = IDThree.dividir_data(dataY, 3)
print(IDThree.obtener_entropia_minima(dataYB))
#segunda divicion a la izquierda
dataYD, dataYE = IDThree.dividir_data(dataYB, 2)
YD, YDE = IDThree.obtener_entropia_minima(dataYD)
print("ENTROPIA 0 EN VARIABLE: ", YD, YDE, " con valor: ", IDThree.obtener_valor(dataYD, YD))#Entropia 0
print(IDThree.obtener_entropia_minima(dataYE))
#tercera divicion a la izquierda (derecho)
dataYH, dataYI = IDThree.dividir_data(dataYE, 10)
print(IDThree.obtener_entropia_variables(dataYH))
YH, YHE = IDThree.obtener_entropia_minima(dataYH)
print("HOLA")
print(dataYH)
print("              \n\n")
print(dataYI)
print("ENTROPIA 0 EN VARIABLE: ", YH, YHE, " con valor: ", IDThree.obtener_valor(dataYH, YH))#Entropia 0
print(IDThree.obtener_entropia_variables(dataYI))
YI, YIE = IDThree.obtener_entropia_minima(dataYI)
print("ENTROPIA 0 EN VARIABLE: ", YI, YIE, " con valor: ", IDThree.obtener_valor(dataYI, YI))#Entropia 0
a, b = IDThree.dividir_data(dataYI, 4)
print("Otra", a, "\n\n")
print(IDThree.obtener_entropia_variables(a))
print(b)
print(IDThree.obtener_entropia_variables(b))



#segunda divicion a la derecha
print(IDThree.obtener_entropia_minima(dataYC))
dataYF, dataYG = IDThree.dividir_data(dataYC, 2)
print("dataYF: ", IDThree.obtener_entropia_minima(dataYF))
#Tercera divicion a la derecha (izquierda)
dataYJ, dataYK = IDThree.dividir_data(dataYF, 8)
print("dataYJ: ", IDThree.obtener_entropia_minima(dataYJ))
#CUARTA DIVICION
dataYN, dataYO = IDThree.dividir_data(dataYJ, 7)
print("dataYN: ", IDThree.obtener_entropia_minima(dataYN))
print("dataYO: ", IDThree.obtener_entropia_minima(dataYO))

YK, YKE = IDThree.obtener_entropia_minima(dataYK)
print("ENTROPIA 0 EN VARIABLE: ", YK, YKE, " con valor: ", IDThree.obtener_valor(dataYK, YK))#Entropia 0


print("dataYG: ",IDThree.obtener_entropia_minima(dataYG))
dataYL, dataYM = IDThree.dividir_data(dataYG, 11)
print("dataYL: ", IDThree.obtener_entropia_minima(dataYL))
#CUARTA DIVICION
dataYP, dataYQ = IDThree.dividir_data(dataYL, 14)
print("dataYP: ", IDThree.obtener_entropia_minima(dataYP))
#QUINTA DIVICION
dataYT, dataYU = IDThree.dividir_data(dataYP, 9)
print("dataYT: ", IDThree.obtener_entropia_minima(dataYT))
print("dataYU: ", IDThree.obtener_entropia_minima(dataYU))



print("dataYQ: ", IDThree.obtener_entropia_minima(dataYQ))
print("dataYM: ", IDThree.obtener_entropia_minima(dataYM))
#CUARTA DIVICION
dataYR, dataYS = IDThree.dividir_data(dataYM, 1)
print("dataYR: ", IDThree.obtener_entropia_minima(dataYR))
print("dataYS: ", IDThree.obtener_entropia_minima(dataYS))




