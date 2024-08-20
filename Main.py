import decition_tree
import data_stract
import IDThree
import Node
import tkinter as tk

#Abrir la base de datos
file_path = "BD.xls"
train_sheet = "E"
test_sheet = "P"

#Extraemos la data de entrenamiento
data = data_stract.get_Data(file_path, train_sheet)

#Extraemos la data de prueba
dataP = data_stract.get_testData(file_path, test_sheet)
#print(dataP)

#Generamos el arbol de desicion
tree = decition_tree.generate_binary_decition_tree(data)

#Preguntas
questions = [
    "Selecciona tu sexo",
    "Tienes emisión de volumen\n excesivo de orina",
    "Tienes aumento anormal de sed",
    "Has tenido pérdida repentina de peso",
    "Has sentido debilidad",
    "Tienes aumento anormal en la\n necesidad de comer",
    "Tienes Flujo, ardor, picazón,\n irritación genital",
    "Tienes visión borrosa",
    "Tienes picazón en la piel,\n que hace que quieras rascarte",
    "Sufres de Irritabilidad",
    "Tienes cicatrización retardada",
    "Tienes disminución de la fuerza,\n debilidad muscular.",
    "Tienes dolor en las articulaciones",
    "Tienes pérdida anormal del cabello",
    "Tienes sobrepeso",
    "Selecciona tu rango de edad"
]


node = tree.root
index, dat = IDThree.obtener_entropia_minima(node.data)

def changeText(index):
    if index==0:
        button1.config(text="Femenino")
        button2.config(text="Masculino")
    elif index == len(questions)-1:
        button1.config(text="menos de 50")
        button2.config(text="más o 50")
    else:
        button1.config(text="Si")
        button2.config(text="No")


# Función que será llamada al presionar el botón
def runTree(answ):
    global node
    if node.left != None:
        if answ == 1:
            node = node.left
        else:
            node = node.right
        index, dat = IDThree.obtener_entropia_minima(node.data)
        changeText(index-1)
        label.config(text=questions[index-1])
    else:
        index, dat = IDThree.obtener_entropia_minima(node.data)
        changeText(index-1)
        clas = Node.Node.getClass(node.data[index])
        if clas == "GREEN":
            strConf = "Test positive"
        elif clas == "RED":
            strConf = "Test negative"
        elif clas == "BLUE":
            if answ ==1:
                strConf = "Test positive"
            else:
                strConf = "Test negative"
        elif clas == "VIOLET":
            if answ ==0:
                strConf = "Test positive"
            else:
                strConf = "Test negative"
        else:
           strConf = "EL SISTEMA NO PUEDE CLASIFICAR ESTA ENTRADA"
        label.config(text=strConf)
        button1.place_forget()
        button2.place_forget()
        buttonE.place(relx=0.5, rely=0.55, anchor='center') 
    return
        
def reboot():
    global node
    node = tree.root
    
    buttonS.place(relx=0.5, rely=0.55, anchor='center') 
    buttonE.place_forget()
    label.config(text="Sistema de detección de diabetes".upper())
    return

def start():
    button1.place(relx=0.5, rely=0.45, anchor='center') 
    button2.place(relx=0.5, rely=0.75, anchor='center') 
    buttonS.place_forget()
    label.config(text=questions[index-1])
    return

boton_estilo = {
    'bg': 'lightblue',        # Color de fondo
    'fg': 'black',            # Color del texto
    'font': ("Montserrat", 12),    # Tipo de fuente y tamaño
    'width': 20,              # Ancho del botón en caracteres
    'height': 2,              # Alto del botón en líneas de texto
    'bd': 4,                  # Ancho del borde
    'relief': 'flat',         # Sin relieve
    'highlightbackground': 'red',  # Color del borde
    'border': 4,                 # Grosor del borde
    'bd':0,
     
}

# Crear la ventana principal
root = tk.Tk()
root.title("ID3-D")
root.geometry("400x230")

# Crear una etiqueta (leyenda)
label = tk.Label(root, text="Sistema de detección de diabetes".upper(), font=("Montserrat", 12))
label.place(relx=0.5, rely=0.2, anchor="center")

# Crear los botones y asociarlos con la función y sus parámetros
button1 = tk.Button(root, text="Si", command=lambda: runTree( 1), **boton_estilo)


button2 = tk.Button(root, text="No",  command=lambda: runTree(0), **boton_estilo)


buttonE = tk.Button(root, text="Regresar al inicio", command=reboot, **boton_estilo)


buttonS  = tk.Button(root, text="Empezar Test",  command=start, **boton_estilo)
buttonS.place(relx=0.5, rely=0.55, anchor='center') 
# Ejecutar el bucle principal de la ventana
root.mainloop()