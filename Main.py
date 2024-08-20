import decition_tree
import data_stract
import IDThree
import Node

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
    "FEMENINO (SI) MASCULINO (NO)"
    "Tienes emisión de volumen excesivo de orina",
    "Tienes aumento anormal de sed",
    "Has tenido pérdida repentina de peso",
    "Has sentido debilidad",
    "Tienes aumento anormal en la necesidad de comer",
    "Tienes Flujo, ardor, picazón, irritación genital",
    "Tienes visión borrosa",
    "Tienes picazón en la piel, que hace que quieras rascarte",
    "Sufres de Irritabilidad",
    "Tienes cicatrización retardada",
    "Tienes disminución de la fuerza, debilidad muscular.",
    "Tienes dolor en las articulaciones",
    "Tienes pérdida anormal del cabello",
    "Tienes sobrepeso",
    "-50 (SI) +=50 (NO)"
]




import tkinter as tk



node = tree.root
index, dat = IDThree.obtener_entropia_minima(node.data)

# Función que será llamada al presionar el botón
def mi_funcion(answ):
    global node
    if node.left != None:
        if answ == 1:
            node = node.left
        else:
            node = node.right
        index, dat = IDThree.obtener_entropia_minima(node.data)
        label.config(text=questions[index-1])
    else:
        index, dat = IDThree.obtener_entropia_minima(node.data)
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
        button1.config(state=tk.DISABLED)
        button2.config(state=tk.DISABLED)
        buttonE.config(state=tk.NORMAL)
    return
        
def reboot():
    global node
    node = tree.root
    
    buttonS.config(state=tk.NORMAL)
    buttonE.config(state=tk.DISABLED)
    label.config(text=questions[index-1])
    return

def start():
    button1.config(state=tk.NORMAL)
    button2.config(state=tk.NORMAL)
    buttonS.config(state=tk.DISABLED)
    label.config(text=questions[index-1])
    return

# Crear la ventana principal
root = tk.Tk()
root.title("Interfaz con funciones")
root.geometry("400x230")

# Crear una etiqueta (leyenda)
label = tk.Label(root, text="Sistema de deteccion de diabetes", font=("Arial", 14))
label.pack(pady=20)

# Crear los botones y asociarlos con la función y sus parámetros
button1 = tk.Button(root, text="Botón 1", width=10, command=lambda: mi_funcion( 1))
button1.pack(pady=5)
button1.config(state=tk.DISABLED)

button2 = tk.Button(root, text="Botón 2", width=10, command=lambda: mi_funcion(0))
button2.pack(pady=5)
button2.config(state=tk.DISABLED)

buttonE = tk.Button(root, text="Regresar al inicio", width=10, command=reboot)
buttonE.pack(pady=8)
buttonE.config(state=tk.DISABLED)

buttonS  = tk.Button(root, text="Empezar Test", width=10, command=start)
buttonS.pack(pady=8)
# Ejecutar el bucle principal de la ventana
root.mainloop()
