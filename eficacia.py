import IDThree
import xlrd
import random



aleatorios = [471, 143, 402, 456, 113, 177, 32, 39, 496, 236, 250, 470, 385, 2, 145, 478, 251, 362, 401, 432, 197, 472, 192, 149, 506, 419, 85, 75, 207, 310, 80, 294, 142, 293, 371, 127, 173, 234, 476, 21, 286, 409, 208, 392, 297, 282, 277, 245, 30, 232, 425, 196, 452, 373, 405, 424, 406, 403, 512, 91, 53, 200, 387, 19, 448, 213, 333, 262, 460, 68, 284, 249, 174, 7, 461, 317, 327, 155, 261, 97, 167, 368, 176, 340, 227, 73, 430, 206, 407, 154, 328, 98, 467, 150, 184, 4, 18, 358, 123, 253, 109, 42, 233, 141, 389, 203, 414, 175, 303, 49, 369, 247, 291, 315, 321, 490, 151, 239, 61, 129, 305, 272, 382, 6, 268, 439, 363, 319, 165, 341, 308, 445, 505, 55, 132, 412, 386, 466, 180, 453, 416, 345, 199, 219, 404, 504, 447, 218, 228, 144, 493, 455, 158, 254, 499, 17, 399, 397, 134, 38, 172, 342, 255, 299, 216, 16, 34, 152, 334, 483, 52, 355, 90, 242, 415, 400, 119, 124, 88, 193, 222, 441, 84, 169, 44, 67, 307, 140, 248, 280, 326, 329, 408, 205, 325, 69, 335, 417, 457, 223, 264, 484, 366, 60, 462, 71, 156, 487, 436, 194, 279, 351, 398, 270, 57, 433, 256, 99, 164, 296, 215, 287, 481, 62, 306, 235, 195, 116, 204, 100, 118, 502, 314, 377, 72, 364, 138, 482, 492, 54, 378, 423, 278, 509, 191, 160, 361, 122, 148, 440, 170, 289, 435, 292, 45, 214, 347, 503, 20, 275, 14, 411, 365, 130, 301, 418, 344, 146, 65, 201, 370, 86, 76, 422, 309, 50, 93, 51, 479, 491, 48, 360, 343, 95, 271, 283, 395, 89, 83, 137, 168, 354, 15, 260, 5, 488, 226, 81, 302, 480, 212, 458, 231, 465, 136, 367, 391, 217, 380, 514, 500, 121, 105, 434, 171, 56, 437, 110, 498, 237, 501, 495, 352, 372, 475, 210, 29, 513, 281, 485, 339, 444, 120, 438, 449, 381, 258, 244, 359, 300, 304, 468, 23, 220, 108, 59, 185, 313, 393, 66, 263, 153, 353, 413, 24, 3, 82, 464, 323, 429, 224, 421, 63, 115, 96, 114, 259, 427, 221, 92, 188, 243, 111, 288, 486, 35, 316, 187, 181, 459, 31, 451, 117, 257, 10, 356, 28, 295, 159, 388, 357, 383, 79, 135, 338, 198, 22, 346, 166, 390, 276, 182, 103, 189, 77, 47, 133, 40, 161, 285, 9, 211, 33, 426, 320, 428, 37, 494, 8, 43, 273, 125, 269, 163, 267, 147, 266, 46, 162, 508, 186, 318, 26, 330, 252, 179, 128, 463, 126, 183, 106, 442, 78, 202, 394, 469, 238, 274, 240, 497, 13, 241, 102, 420, 64, 225, 336, 178, 322, 312, 94, 446, 87, 348, 507, 70, 510, 25, 131, 12, 265, 290, 474, 332, 157, 101, 311, 41, 107, 473, 229, 58, 477, 36, 246, 349, 11, 298, 112, 375, 209, 190, 384, 374, 337, 376, 511, 450, 396, 443, 431, 379, 104, 27, 324, 350, 489, 410, 139, 454, 331, 230, 74]

#359 es el 70% de los datos (se toman los primeros 359 numeros aleatorios)
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
        15: None,
    }

dataPrueba = {
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
    }

for i in range(2, sheet.ncols):
    variable = []
    for num in range(0, 359):
        clase = 0
        valor = 0
        if(sheet.cell_value(aleatorios[num], 1) == "Positive"):
            clase = 1
        if(sheet.cell_value(aleatorios[num], i) == "Yes" or sheet.cell_value(aleatorios[num], i)=="Female"):
            valor = 1
        elemento = [clase, valor]
        variable.append(elemento)
    data[i-1] = variable

for i in range(2, sheet.ncols):
    variable = []
    for num in range(359, 513):
        clase = 0
        valor = 0
        if(sheet.cell_value(aleatorios[num], 1) == "Positive"):
            clase = 1
        if(sheet.cell_value(aleatorios[num], i) == "Yes" or sheet.cell_value(aleatorios[num], i)=="Female"):
            valor = 1
        elemento = [clase, valor]
        variable.append(elemento)
    dataPrueba[i-1] = variable

#---------------Generamos arbol de nuevo set de datos
    
print(IDThree.obtener_entropia_minima(data))
dataB, dataC = IDThree.dividir_data(data, 3)

print(IDThree.obtener_entropia_minima(dataB))
print(IDThree.obtener_entropia_minima(dataC))

dataD, dataE = IDThree.dividir_data(dataB, 2)
dataF, dataG = IDThree.dividir_data(dataC, 1)

print(IDThree.obtener_entropia_minima(dataD))
print(IDThree.obtener_entropia_minima(dataE))
print(IDThree.obtener_entropia_minima(dataF))
print(IDThree.obtener_entropia_minima(dataG))

dataH, dataI = IDThree.dividir_data(dataE, 10)
dataJ, dataK = IDThree.dividir_data(dataF, 14)
dataL, dataM = IDThree.dividir_data(dataG, 2)

print("TERCER NIVEL\n", IDThree.obtener_entropia_minima(dataH))
print(IDThree.obtener_entropia_minima(dataI))
print(IDThree.obtener_entropia_minima(dataJ))
print(IDThree.obtener_entropia_minima(dataK))
print(IDThree.obtener_entropia_minima(dataL))
print(IDThree.obtener_entropia_minima(dataM))

dataN, dataO = IDThree.dividir_data(dataI, 8)
dataP, dataQ = IDThree.dividir_data(dataK, 8)
dataR, dataS = IDThree.dividir_data(dataL, 15)
dataT, dataU = IDThree.dividir_data(dataM, 10)

print("NIVEL 4\n",IDThree.obtener_entropia_minima(dataN))
print(IDThree.obtener_entropia_minima(dataO))
print(IDThree.obtener_entropia_minima(dataP))
print(IDThree.obtener_entropia_minima(dataQ))
print(IDThree.obtener_entropia_minima(dataR))
print(IDThree.obtener_entropia_minima(dataS))
print(IDThree.obtener_entropia_minima(dataT))
print(IDThree.obtener_entropia_minima(dataU))

dataV, dataW = IDThree.dividir_data(dataO, 12)
dataX, dataY = IDThree.dividir_data(dataQ, 13)
dataZ, dataA1 = IDThree.dividir_data(dataS, 13)
dataB1, dataC1 = IDThree.dividir_data(dataT, 7)
dataD1, dataE1 = IDThree.dividir_data(dataU, 5)

print("NIVEL 5", IDThree.obtener_entropia_minima(dataV))
print(IDThree.obtener_entropia_minima(dataW))
print(IDThree.obtener_entropia_minima(dataX))
print(IDThree.obtener_entropia_minima(dataY))
print(IDThree.obtener_entropia_minima(dataZ))
print(IDThree.obtener_entropia_minima(dataA1))
print(IDThree.obtener_entropia_minima(dataB1))
print(IDThree.obtener_entropia_minima(dataC1))
print(IDThree.obtener_entropia_minima(dataD1))
print(IDThree.obtener_entropia_minima(dataE1))

dataF1, dataG1 = IDThree.dividir_data(dataY, 12)
dataH1, dataI1 = IDThree.dividir_data(dataC1, 6)
dataJ1, dataK1 = IDThree.dividir_data(dataD1, 13)

print("NIVEL 6", IDThree.obtener_entropia_minima(dataF1))
print(IDThree.obtener_entropia_minima(dataG1))
print(IDThree.obtener_entropia_minima(dataH1))
print(IDThree.obtener_entropia_minima(dataI1))
print(IDThree.obtener_entropia_minima(dataJ1))
print(IDThree.obtener_entropia_minima(dataK1))

dataL1, dataM1 = IDThree.dividir_data(dataG1, 2)
dataN1, dataO1 = IDThree.dividir_data(dataK1, 6)
print("NIVEL 7", IDThree.obtener_entropia_minima(dataL1))
print(IDThree.obtener_entropia_minima(dataM1))
print(IDThree.obtener_entropia_minima(dataN1))
print(IDThree.obtener_entropia_minima(dataO1))

dataP1, dataQ1 = IDThree.dividir_data(dataM1, 15)
print("NIVEL 8",IDThree.obtener_entropia_minima(dataP1))
print(IDThree.obtener_entropia_minima(dataQ1))