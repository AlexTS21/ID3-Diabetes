import xlrd

def get_variables(path):
    file_path = "BASE_ORIGINAL.xls"

    openFile = xlrd.open_workbook(file_path)

    sheet = openFile.sheet_by_name("diabetes_data_upload")

    dataY = {
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

    dataO = {
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
        variableO = []
        variableY = []
        for j in range(1, sheet.nrows):
            clase = 0
            valor = 0
            if(sheet.cell_value(j, 1) == "Positive"):
                clase = 1
            if(sheet.cell_value(j, i) == "Yes" or sheet.cell_value(j, i)=="Female"):
                valor = 1
            elemento = [clase, valor]
            if(int(sheet.cell_value(j, 0)) < 50):
                variableO.append(elemento)
            else:
                variableY.append(elemento)
        dataY[i-1] = variableY
        dataO[i-1] = variableO

    return dataY, dataO