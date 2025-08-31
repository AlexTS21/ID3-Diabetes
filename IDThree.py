from .entropia import entropia_variable

def obtener_entropia_variables(data):
    entropias = {}
    for variable in data.values():
        entropias[list(data.keys())[list(data.values()).index(variable)]] = entropia_variable(variable)
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
    data[parametro] = var
    order_dic(data)
    return data1, data0

def order_dic(dic):
    keys = []
    sorted_dict = {}
    for key in dic.keys():
        keys.append(key)
    sorted_keys = sorted(keys)

    for element in sorted_keys:
        sorted_dict[element] = dic[element]
    dic.clear()
    for element in sorted_keys:
        dic[element] = sorted_dict[element]
    

    
def get_num_clase(variable):
    lis = []
    for element in variable:
        if element[0] not in lis:
            lis.append(element[0])
    return len(lis)


def iterable_data(data):
    if(len(data) < 2):
        return False
    for variable in data.values():
        if(len(variable) == 0):
            return False
    return True