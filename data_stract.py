import xlrd

#DEVUELVE UN DICCIONARIO CON LOS DATOS
def get_Data(path, sheet_op):
    openFile = xlrd.open_workbook(path)
    sheet = openFile.sheet_by_name(sheet_op)

    data={}
    for i in range(1, sheet.ncols):
        data[i] = None  

    for i in range(1, sheet.ncols):
        variable = []
        for j in range(1, sheet.nrows):
            clase = 0
            valor = 0
            if(sheet.cell_value(j, 0) == "Positive"):
                clase = 1
            if(sheet.cell_value(j, i) == "Yes" or sheet.cell_value(j, i)=="Female"):
                valor = 1
            if(int(sheet.cell_value(j, sheet.ncols-1)) < 50 and i==sheet.ncols-1):
                valor = 1 
            elemento = [clase, valor]
            variable.append(elemento)
        data[i] = variable
    del openFile
    return data

#DEVUELVE LISTA CON TUPLAS (CLASE, DICCIONARIO CON CAMINO)
def get_testData(path, sheet_op):
    openFile = xlrd.open_workbook(path)
    sheet = openFile.sheet_by_name(sheet_op)
    dataP = []

    for i in range(1, sheet.nrows):
        tup = []
        tup.append(0)
        dataPI = {}
        for r in range(1, sheet.ncols):
            dataPI[r] = None 
        
        for j in range(1, sheet.ncols):
            dataPI[j] = 0
            if sheet.cell_value(i,j) == "Yes" or sheet.cell_value(i, j)=="Female":
                dataPI[j] = 1
            if int(sheet.cell_value(i, sheet.ncols-1)) <50 and j == sheet.ncols-1:
                dataPI[j] = 1
        if(sheet.cell_value(i, 0) == "Positive" ):
            tup[0]  = 1
        tup.append(dataPI)
        dataP.append(tup)
    del openFile
    
    return dataP