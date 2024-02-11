import xlrd
import IDThree

file_path = "BASE_ORIGINAL.xls"

openFile = xlrd.open_workbook(file_path)

sheet = openFile.sheet_by_name("diabetes_data_upload")

data = {
    1: None,
    2: None,
    3: None,
    4: None,
    5: None,
    6: None,
    7: None,
    8: None,
    9: None,
    10: None,
    11: None,
    12: None,
    13: None,
    14: None,

}

print(sheet.nrows)

for i in range(3, sheet.ncols):
    variable = []
    for j in range(1, sheet.nrows):
        clase = 0
        valor = 0
        if(sheet.cell_value(j, 1) == "Positive"):
            clase = 1
        if(sheet.cell_value(j, i) == "Yes"):
            valor = 1
        elemento = [clase, valor]
        variable.append(elemento)
    data[i-2] = variable

print(IDThree.obtener_entropia_variables(data))
print(IDThree.obtener_entropia_minima(data))

#Pirmera divicion 
data1Iz, data1De = IDThree.dividir_data(data, 1)

print("Para divicion a izquierda: ")
print(IDThree.obtener_entropia_variables(data1Iz))
print(IDThree.obtener_entropia_minima(data1Iz))

print("Para divicion a derecha: ")
print(IDThree.obtener_entropia_variables(data1De))
print(IDThree.obtener_entropia_minima(data1De))

#Segunda divicion
#Lado izquierdo
data2IZIz, data2IZDe = IDThree.dividir_data(data1Iz, 2)

print("Para divicion a izquierda: ")
#print(data2IZIz)
print(IDThree.obtener_entropia_variables(data2IZIz))
mini = IDThree.obtener_entropia_minima(data2IZIz)
print("HOla", IDThree.obtener_valor(data2IZIz, mini))

print("Para divicion a derecha: ")
print(IDThree.obtener_entropia_variables(data2IZDe))
print(IDThree.obtener_entropia_minima(data2IZDe))


#Lado derecho
data2DEIz, data2DEDe = IDThree.dividir_data(data1De, 2)
print("Para divicion a izquierda: ")
#print(data2IZIz)
print(IDThree.obtener_entropia_variables(data2DEIz))
print(IDThree.obtener_entropia_minima(data2DEIz))

print("Para divicion a derecha: ")
print(IDThree.obtener_entropia_variables(data2DEDe))
print(IDThree.obtener_entropia_minima(data2DEDe))

