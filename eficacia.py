import IDThree
import xlrd
import random
import decition_tree
from Node import Node


#aleatorios = [471, 143, 402, 456, 113, 177, 32, 39, 496, 236, 250, 470, 385, 2, 145, 478, 251, 362, 401, 432, 197, 472, 192, 149, 506, 419, 85, 75, 207, 310, 80, 294, 142, 293, 371, 127, 173, 234, 476, 21, 286, 409, 208, 392, 297, 282, 277, 245, 30, 232, 425, 196, 452, 373, 405, 424, 406, 403, 512, 91, 53, 200, 387, 19, 448, 213, 333, 262, 460, 68, 284, 249, 174, 7, 461, 317, 327, 155, 261, 97, 167, 368, 176, 340, 227, 73, 430, 206, 407, 154, 328, 98, 467, 150, 184, 4, 18, 358, 123, 253, 109, 42, 233, 141, 389, 203, 414, 175, 303, 49, 369, 247, 291, 315, 321, 490, 151, 239, 61, 129, 305, 272, 382, 6, 268, 439, 363, 319, 165, 341, 308, 445, 505, 55, 132, 412, 386, 466, 180, 453, 416, 345, 199, 219, 404, 504, 447, 218, 228, 144, 493, 455, 158, 254, 499, 17, 399, 397, 134, 38, 172, 342, 255, 299, 216, 16, 34, 152, 334, 483, 52, 355, 90, 242, 415, 400, 119, 124, 88, 193, 222, 441, 84, 169, 44, 67, 307, 140, 248, 280, 326, 329, 408, 205, 325, 69, 335, 417, 457, 223, 264, 484, 366, 60, 462, 71, 156, 487, 436, 194, 279, 351, 398, 270, 57, 433, 256, 99, 164, 296, 215, 287, 481, 62, 306, 235, 195, 116, 204, 100, 118, 502, 314, 377, 72, 364, 138, 482, 492, 54, 378, 423, 278, 509, 191, 160, 361, 122, 148, 440, 170, 289, 435, 292, 45, 214, 347, 503, 20, 275, 14, 411, 365, 130, 301, 418, 344, 146, 65, 201, 370, 86, 76, 422, 309, 50, 93, 51, 479, 491, 48, 360, 343, 95, 271, 283, 395, 89, 83, 137, 168, 354, 15, 260, 5, 488, 226, 81, 302, 480, 212, 458, 231, 465, 136, 367, 391, 217, 380, 514, 500, 121, 105, 434, 171, 56, 437, 110, 498, 237, 501, 495, 352, 372, 475, 210, 29, 513, 281, 485, 339, 444, 120, 438, 449, 381, 258, 244, 359, 300, 304, 468, 23, 220, 108, 59, 185, 313, 393, 66, 263, 153, 353, 413, 24, 3, 82, 464, 323, 429, 224, 421, 63, 115, 96, 114, 259, 427, 221, 92, 188, 243, 111, 288, 486, 35, 316, 187, 181, 459, 31, 451, 117, 257, 10, 356, 28, 295, 159, 388, 357, 383, 79, 135, 338, 198, 22, 346, 166, 390, 276, 182, 103, 189, 77, 47, 133, 40, 161, 285, 9, 211, 33, 426, 320, 428, 37, 494, 8, 43, 273, 125, 269, 163, 267, 147, 266, 46, 162, 508, 186, 318, 26, 330, 252, 179, 128, 463, 126, 183, 106, 442, 78, 202, 394, 469, 238, 274, 240, 497, 13, 241, 102, 420, 64, 225, 336, 178, 322, 312, 94, 446, 87, 348, 507, 70, 510, 25, 131, 12, 265, 290, 474, 332, 157, 101, 311, 41, 107, 473, 229, 58, 477, 36, 246, 349, 11, 298, 112, 375, 209, 190, 384, 374, 337, 376, 511, 450, 396, 443, 431, 379, 104, 27, 324, 350, 489, 410, 139, 454, 331, 230, 74]

#359 es el 70% de los datos (se toman los primeros 359 numeros aleatorios)
file_path = "data_G.xls"

openFile = xlrd.open_workbook(file_path)

sheet = openFile.sheet_by_name("E")

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
        15: None,
        16: None,
    }


#Extraemos la data de entrenamiento

for i in range(2, sheet.ncols):
    variable = []
    for j in range(1, sheet.nrows):
        clase = 0
        valor = 0
        if(sheet.cell_value(j, 1) == "Positive"):
            clase = 1
        if(sheet.cell_value(j, i) == "Yes" or sheet.cell_value(j, i)=="Female"):
            valor = 1
        if(int(sheet.cell_value(j, 0)) < 50 and i==17):
            valor = 1 
        elemento = [clase, valor]
        variable.append(elemento)
    data[i-1] = variable


#Extraemos la data de prueba
dataP = []
sheet2 =  openFile.sheet_by_name("P")
for i in range(1, sheet2.nrows):
    tup = []
    tup.append(0)
    dataPI = {
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
            15: None,
            16: None,
        }
    for j in range(2, sheet2.ncols):
        dataPI[j-1] = 0
        if sheet2.cell_value(i,j) == "Yes" or sheet2.cell_value(i, j)=="Female":
            dataPI[j-1] = 1
        if int(sheet2.cell_value(i,0)) <50 and j == 17:
            dataPI[j-1] = 1
    if(sheet2.cell_value(i, 1) == "Positive" ):
        tup[0]  = 1
    tup.append(dataPI)
    dataP.append(tup)



##---------------Generamos arbol de nuevo set de datos

tree = decition_tree.generate_binary_decition_tree(data)
tree.printTree()

#correcrto = 0
#for element in dataP:
#    if element[0] == tree.test_path(element[1]):
#       correcrto+=1
#
#print("LA EFICIENCIA ES: ", correcrto/len(dataP), "Aciertos ",  correcrto, " de ", len(dataP))

#print(IDThree.obtener_entropia_minima(data))
#dataA, dataB = IDThree.dividir_data(data, 2)
#
#print(IDThree.obtener_entropia_minima(dataA))
#dataC, dataD = IDThree.dividir_data(dataA, 3)
#print(IDThree.obtener_entropia_minima(dataC))
#print(IDThree.obtener_entropia_minima(dataD))
#
#
#
#print(IDThree.obtener_entropia_minima(dataB))
#dataE, dataF = IDThree.dividir_data(dataB, 3)
#print(IDThree.obtener_entropia_minima(dataE))
#print(IDThree.obtener_entropia_minima(dataF))
#
#print("NIVEL  3")
#dataG, dataH = IDThree.dividir_data(dataD, 9)
#print(IDThree.obtener_entropia_minima(dataG))
#print(IDThree.obtener_entropia_minima(dataH))
#
#dataI, dataJ = IDThree.dividir_data(dataE, 10)
#print(IDThree.obtener_entropia_minima(dataI))
#print(IDThree.obtener_entropia_minima(dataJ))
#
#dataK, dataL = IDThree.dividir_data(dataF, 1)
#print(IDThree.obtener_entropia_minima(dataK))
#print(IDThree.obtener_entropia_minima(dataL))
#
#print("NIVEL 4")
#dataM, dataN = IDThree.dividir_data(dataG, 7)
#print(IDThree.obtener_entropia_minima(dataM))
#print(IDThree.obtener_entropia_minima(dataN))
#
#dataO, dataP = IDThree.dividir_data(dataJ, 13)
#print(IDThree.obtener_entropia_minima(dataO))
#print(IDThree.obtener_entropia_minima(dataP))
#
#dataQ, dataR = IDThree.dividir_data(dataK, 14)
#print(IDThree.obtener_entropia_minima(dataQ))
#print(IDThree.obtener_entropia_minima(dataR))
#
#dataS, dataT = IDThree.dividir_data(dataL, 10)
#print(IDThree.obtener_entropia_minima(dataS))
#print(IDThree.obtener_entropia_minima(dataT))
#
#print("NIVEL 5")
#dataU, dataV = IDThree.dividir_data(dataM, 15)
#print(IDThree.obtener_entropia_minima(dataU))
#print(IDThree.obtener_entropia_minima(dataV))
#
#dataW, dataX = IDThree.dividir_data(dataR, 8)
#print(IDThree.obtener_entropia_minima(dataW))
#print(IDThree.obtener_entropia_minima(dataX))
#
#dataY, dataZ = IDThree.dividir_data(dataS, 7)
#print(IDThree.obtener_entropia_minima(dataY))
#print(IDThree.obtener_entropia_minima(dataZ))
#
#dataA1, dataB1 = IDThree.dividir_data(dataT, 11)
#print(IDThree.obtener_entropia_minima(dataA1))
#print(IDThree.obtener_entropia_minima(dataB1))
#
#print("NIVEL 6")
#dataC1, dataD1 = IDThree.dividir_data(dataX, 5)
#print(IDThree.obtener_entropia_minima(dataC1))
#print(IDThree.obtener_entropia_minima(dataD1))
#
#dataE1, dataF1 = IDThree.dividir_data(dataZ, 6)
#print(IDThree.obtener_entropia_minima(dataE1))
#print(IDThree.obtener_entropia_minima(dataF1))
#
#dataG1, dataH1 = IDThree.dividir_data(dataA1, 16)
#print(IDThree.obtener_entropia_minima(dataG1))
#print(IDThree.obtener_entropia_minima(dataH1))
#
#dataI1, dataJ1 = IDThree.dividir_data(dataB1, 12)
#print(IDThree.obtener_entropia_minima(dataI1))
#print(IDThree.obtener_entropia_minima(dataJ1))
#
#print("NIVEL 7")
#dataK1, dataL1 = IDThree.dividir_data(dataD1, 16)
#print(IDThree.obtener_entropia_minima(dataK1))
#print(IDThree.obtener_entropia_minima(dataL1))
#
#dataM1, dataN1 = IDThree.dividir_data(dataG1, 6)
#print(IDThree.obtener_entropia_minima(dataM1))
#print(IDThree.obtener_entropia_minima(dataN1))
#
#print("NIVEL 8")
#dataO1, dataP1 = IDThree.dividir_data(dataK1, 15)
#print(IDThree.obtener_entropia_minima(dataO1))
#print(IDThree.obtener_entropia_minima(dataP1))
#
#dataQ1, dataR1 = IDThree.dividir_data(dataN1, 9)
#print(IDThree.obtener_entropia_minima(dataQ1))
#print(IDThree.obtener_entropia_minima(dataR1))
#
#print("NIVEL 9")
#dataS1, dataT1 = IDThree.dividir_data(dataP1, 4)
#print(IDThree.obtener_entropia_minima(dataS1))
#print(IDThree.obtener_entropia_minima(dataT1))
#
#print("NIVEL 10")
#dataU1, dataV1 = IDThree.dividir_data(dataT1, 6)
#print(IDThree.obtener_entropia_minima(dataU1))
#print(IDThree.obtener_entropia_minima(dataV1))
#
#print(IDThree.iterable_data(dataV1))