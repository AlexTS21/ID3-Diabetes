import xlrd

def get_variables(path, sheet_op):

    openFile = xlrd.open_workbook(path)

    sheet = openFile.sheet_by_name(sheet_op)

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


    for i in range(2, sheet.ncols):
        variable = []
        for j in range(1, sheet.nrows):
            clase = 0
            valor = 0
            if(sheet.cell_value(j, 1) == "Positive"):
                clase = 1
            if(sheet.cell_value(j, i) == "Yes" or sheet.cell_value(j, i)=="Female"):
                valor = 1
            if(int(sheet.cell_value(j, 0)) < 50 and i==16):
                valor = 1 
            elemento = [clase, valor]
            variable.append(elemento)
        data[i-1] = variable
      

    return data

def data_stact_prueba(path, sheet_op):
    openFile = xlrd.open_workbook(path)

    sheet = openFile.sheet_by_name(sheet_op)
    dataYL = []
    dataOL = []
    for i in range(1, sheet.nrows):
        tup = []
        tup.append(0)
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
        for j in range(2, sheet.ncols):
            data[j-1] = 0
            if sheet.cell_value(i,j) == "Yes":
                data[j-1] = 1
        if(sheet.cell_value(i, 1) == "Positive" ):
            tup[0]  = 1
        tup.append(data)
        if(sheet.cell_value(i,0) < 50):
            dataYL.append(tup)
        else:
            dataOL.append(tup)

    return dataYL, dataOL




