import Entropia
import BinaryTree

A1= [[1,1],[1,1],[0,1],[0,1],[0,1],[0,1]]
A2 = [[1,1],[1,0],[0,0],[0,0],[0,0],[0,0]]
A3 = [[1,0],[1,0], [0,0], [0,0], [0,0]]
A4= [[1,1],[1,0],[0,1],[0,0],[0,1],[0,0]]
A5 = [[1,1],[1,0],[0,1], [0,1], [0,0], [0,0]]

variables = [A1, A2, A3, A4, A5]

def obtener_entropia_variables(data):
    entropias = {}
    i = 1
    for variable in data:
        entropias[i] = Entropia.entropia_variable(variable)
        i+=1
    return entropias

def obtener_entropia_minima(data):
    entropias = obtener_entropia_variables(data)
    return min(entropias, key=entropias.get)

#ELIMINA DEL SET DE DATOS UNA VARIABLE Y LA DEVUELVE
def eliminar_variable(data, variable):
    var = data[variable-1]
    data.remove(var)    
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
    data1 = []
    data0 = []
    for variable in data:
        var0 = []
        var1 = []
        for elemento in variable:
            if(variable.index(elemento) in var0):
                var0.append(elemento)
            else:
                var1.append(elemento)
        data1.append(var1)
        data0.append(var0)
    return data1, data0

print(obtener_entropia_variables(variables))
print(obtener_entropia_minima(variables))

data1, data2 = dividir_data(variables, obtener_entropia_minima(variables))

print(data1)
print(data2)

