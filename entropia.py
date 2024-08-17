import math

#LAS VARIABLES SON UNA LISTA QUE CONTIENE UNA LISTA CON 2 ELEMENTOS (CLASE A LA QUE PERTENECEN)(VALOR QUE TOMA)
#A1= [[1,1],[1,1],[0,1],[0,1],[0,1],[0,1], [2,0], [2,0], [2,0], [2,0], [3,1], [3,1]]
#A2 = [[1,1],[1,1],[0,0],[0,0],[0,0],[0,0], [2, 1], [2, 1], [2, 1], [2, 1], [3,0], [3,0]]
#A3 = [[1,0],[1,0], [2,0], [2,0], [2,0], [2,0], [3,0], [3,0], [3,0], [3,0], [4,1], [4,1]]
#A4= [[1,1],[1,0],[0,1],[0,0],[0,1],[0,0],[2,1],[2,0],[2,1],[2,0],[3,1],[3,0]]
#A5 = [[1,1],[1,0],[2,1], [2,1], [2,0], [2,0], [3,1], [3,1], [3,0], [3,0], [4,1], [4,1] ]

#PROBABILIDAD DE UN VALOR X SEA TOMADO EN UNA VARIABLE
#FUNCIONES QUE UTILIZA: contar_valor
def probabilidad_valor_en_variable(variable, valor):
    return contar_valor(variable, valor)/len(variable)

#CUENTA UN VALOR X EN UNA VARIBALE
def contar_valor(variable, valor):
    contador = 0
    for element in variable:
        if(element[1] == valor):
            contador = contador+1
    return contador

#CUENTA CUANTOS VALORES X DE UNA VARIABLE HAY EN UNA CLASE
def contar_clase(variable, valor, clase):
    contador = 0
    for element in variable:
        if(element[0] == clase):
            if(element[1] == valor):
                contador = contador+1
    return contador

#CUENTA CUANTOS ELEMENTOS CONTIENE UNA CLASE
def tamano_clase(variable, clase):
    contador = 0
    for elemento in variable:
        if(elemento[0] == clase):
            contador = contador +1
    return contador

#CALCULA LA PROBABILIDAD DE QUE LA VARIABLE TOME UN VALOR X EN UNA CLASE (VALORES X EN CALSE/TOTAL DE ELMETNOS EN CLASE)
#FUNCIONES QUE UTILIZA:contar_clase, contar_valor
def probabilidad_condicional(variable, valor, clase):
    p = 0 
    if(contar_valor(variable, valor) != 0):
        p=contar_clase(variable, valor, clase)/contar_valor(variable, valor)
    if(p!=0):
        return p*math.log(p,2)
    else:
        return 0

#TOTAL DE CLASES QUE EXISTEN
#FUNCIONES QUE UTILIZA: obtener_clases
def total_clases(variable):
    c = obtener_clases(variable)
    return len(c)

#DEVUELVE UNA LISTA CON LAS CALSES QUE HAY
def obtener_clases(variable):
    c = list()
    for elemento in variable:
        if(not(elemento[0] in c)):
            c.append(elemento[0])
    return c

#SUMATORIA DE LA ENTROPIA DE UNA CLASE TOMANDO UN VALOR X
#FUNCIONES QUE UTILIZA: obtener_clases, probabilidad_condicional
def sumatoria_entropia_clases_variable(variable, valor):
    resultado = 0
    for elemento in obtener_clases(variable):
        resultado = resultado + probabilidad_condicional(variable, valor, elemento)
    return resultado

#CALCULO DE ENTROPIA PARA UNA VARIABLE CONSIDERANDO SOLO VALORES BINARIOS (0,1)
#FUNCIONES QUE UTILIZA: probabilidad_valor_en_variable
def entropia_variable(variable):
    valor_uno = probabilidad_valor_en_variable(variable, 1)*sumatoria_entropia_clases_variable(variable, 1)
    valor_cero = probabilidad_valor_en_variable(variable, 0)*sumatoria_entropia_clases_variable(variable, 0)
    return abs(valor_cero + valor_uno)

#CALCULA LA PROBABILIDAD DE CLASE (ELEMENTOS DE LA CLASE/TOTAL DE ELEMETNOS)
#FUNCIONES QUE UTILIZA: tamaño_clase
def probabilidad_clase(vector, clase):
    return tamano_clase(vector, clase)/len(vector)

#CALUCLA LA ENTROPIA DE UNA CLASE A TRAVES DE SU PROBABILIDAD (ELEMENTOS DE LA CLASE/TOTAL DE ELEMETNOS)
#FUNCIONES QUE UTILIZA: probabilidad_clase
def entropia_clase(vector, clase):
    p = probabilidad_clase(vector, clase)
    if(p!=0):
        return p*math.log(p,2)
    else:
        return 0

#CALCULA LA ENTROPIA GENERAL DE UN CONJUNTO DE DATOS A TRAVES DE LA SUMATORIA DE LA ENTROPIA DE CADA CLASE
#FUNCIONES QUE UTILIZA: entropia_clase, clases
def entropia_general(vector):
    entropia = 0
    c = obtener_clases(vector)
    for elemento in c:
        entropia = entropia + entropia_clase(vector, elemento)
    return abs(entropia)
