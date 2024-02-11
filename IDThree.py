import Entropia
import BinaryTree

A1= [[1,1],[1,1],[0,1],[0,1],[0,1],[0,1]]
A2 = [[1,1],[1,0],[0,0],[0,0],[0,0],[0,0]]
A3 = [[1,0],[1,0], [0,0], [0,0], [0,0]]
A4= [[1,1],[1,0],[0,1],[0,0],[0,1],[0,0]]
A5 = [[1,1],[1,0],[0,1], [0,1], [0,0], [0,0]]

variables = {
    1 : A1,
    2 : A2,
    3 : A3,
    4 : A4,
    5 : A5
}

def obtener_entropia_variables(data):
    entropias = {}
    for variable in data.values():
        entropias[list(data.keys())[list(data.values()).index(variable)]] = Entropia.entropia_variable(variable)
    return entropias


def obtener_entropia_minima(data):
    entropias = obtener_entropia_variables(data)
    key = min(entropias, key=entropias.get)
    return key, entropias[key]

def obtener_valor(data, key):
    variable = data[key]
    return variable[0][0]

#ELIMINA DEL SET DE DATOS UNA VARIABLE Y LA DEVUELVE
def eliminar_variable(data, variable):
    var = data[variable]
    data.pop(variable)    
    return var

#OBTINE LOS INDICES DE UN VALOR X EN UNA VARIABLE
def obtener_indices(variable):
    in1 = []
    in0 = []
    i = 0
    for elemento in variable:
        if(elemento[1]  == 0):
            in0.append(i)
        else:
            in1.append(i)
        i+=1
    return in1, in0

#DEVUELVE DOS SET DE DATOS DIVIDIDOS RESPECTO A UN PARAMETRO (VARIABLE)
def dividir_data(data, parametro):
    var = eliminar_variable(data, parametro)
    in1, in0 = obtener_indices(var)
    data1 = {}
    data0 = {}
    for variable in data.values():
        var0 = []
        var1 = []
        i=0
        for elemento in variable:
            if(i in in0):
                var0.append(elemento)
            else:
                var1.append(elemento)
            i+=1
        data1[list(data.keys())[list(data.values()).index(variable)]]=var1
        data0[list(data.keys())[list(data.values()).index(variable)]]=var0
    return data1, data0

#print(obtener_entropia_variables(variables))
#print(obtener_entropia_minima(variables))
#
#data1, data2 = dividir_data(variables, 2)
#
#print("DATAAAAA 1")
#print(data1)
#print(data2)
#
#print("ENTROPIASSS")
#print(obtener_entropia_variables(data1))
#print(obtener_entropia_minima(data1))
#print("DATA 2")
#print(obtener_entropia_variables(data2))
#print(obtener_entropia_minima(data2))
#
#data3, data4 = dividir_data(data2, 4)
#print("ENTROPIASS2")
#print(obtener_entropia_variables(data3))
#print(obtener_entropia_minima(data3))
#print("DATA 4")
#print(obtener_entropia_variables(data4))
#print(obtener_entropia_minima(data4))
#
#
#data5, data6 =dividir_data(data4, 5)
#print("ENTROPIASS3")
#print(obtener_entropia_variables(data5))
#print(obtener_entropia_minima(data5))
#print("DATA 4")
#print(obtener_entropia_variables(data6))
#print(obtener_entropia_minima(data6))

#print(obtener_entropia_variables(variables))
#key = obtener_entropia_minima(variables)
#print(obtener_valor(variables, key))
