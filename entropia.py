import math

A1= [[1,1],[1,1],[0,1],[0,1],[0,1],[0,1], [2,0], [2,0], [2,0], [2,0], [3,1], [3,1]]
A2 = [[1,1],[1,1],[0,0],[0,0],[0,0],[0,0], [2, 1], [2, 1], [2, 1], [2, 1], [3,0], [3,0]]
A3 = [[1,0],[1,0], [2,0], [2,0], [2,0], [2,0], [3,0], [3,0], [3,0], [3,0], [4,1], [4,1]]
A4= [[1,1],[1,0],[0,1],[0,0],[0,1],[0,0],[2,1],[2,0],[2,1],[2,0],[3,1],[3,0]]
A5 = [[1,1],[1,0],[2,1], [2,1], [2,0], [2,0], [3,1], [3,1], [3,0], [3,0], [4,1], [4,1] ]

#PROBABILIDAD DE UN VALOR X EN GENERAL
def probabilidad_total(arreglo, valor):
    return contar_valor(arreglo, valor)/len(arreglo)

#CUENTA UN VALOR X EN GENERAL
def contar_valor(arreglo, valor):
    contador = 0
    for element in arreglo:
        if(element[1] == valor):
            contador = contador+1
    return contador

#CUENTA CUANTOS VALORES X EN UNA CLASE
def contar_clase(arreglo, valor, clase):
    contador = 0
    for element in arreglo:
        if(element[0] == clase):
            if(element[1] == valor):
                contador = contador+1
    return contador

#CUENTA CUANTOS ELEMENTOS PERTENECEN A UNA CLASE
def tamaño_clase(arreglo, clase):
    contador = 0
    for elemento in arreglo:
        if(elemento[0] == clase):
            contador = contador +1
    return contador

#PROBABILIDAD CONDCIONAL
def probabilidad_condicional(arreglo, valor, clase):
    p = contar_clase(arreglo, valor, clase)/contar_valor(arreglo, valor)
    if(p!=0):
        return p*math.log(p,2)
    else:
        return 0

#TOTAL DE CLASES QUE EXISTEN
def total_clases(arreglo):
    c = clases(arreglo)
    return len(c)

#DEVUELVE UNA LISTA CON LAS CALSES QUE HAY
def clases(arreglo):
    c = list()
    for elemento in arreglo:
        if(not(elemento[0] in c)):
            c.append(elemento[0])
    return c

#SUMATORIA DE CALSES
def sumatoria_clases(arreglo, valor):
    resultado = 0
    
    for elemento in clases(arreglo):
        resultado = resultado + probabilidad_condicional(arreglo, valor, elemento)
    return resultado

#CALCULO DE ENTROPIA PARA UNA VARIABLE A BITS
def entropia_variable(variable):
    valor_uno = probabilidad_total(variable, 1)*sumatoria_clases(variable, 1)
    valor_cero = probabilidad_total(variable, 0)*sumatoria_clases(variable, 0)
    return abs(valor_cero + valor_uno)

#PROBABILIDAD DE UNA CLASE
def probabilidad_clase(vector, clase):
    return tamaño_clase(vector, clase)/len(vector)

#ENTROPIA DE LA CLASE
def entropia_clase(vector, clase):
    p = probabilidad_clase(vector, clase)
    if(p!=0):
        return p*math.log(p,2)
    else:
        return 0

def entropia_general(vector):
    entropia = 0
    c = clases(vector)
    for elemento in c:
        entropia = entropia + entropia_clase(vector, elemento)
    return abs(entropia)


print(entropia_variable(A1))
print(entropia_variable(A2))
print(entropia_variable(A3))
print(entropia_variable(A4))
print(entropia_variable(A5))

print(entropia_general(A1))

