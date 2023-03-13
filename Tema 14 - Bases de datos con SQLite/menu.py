import sqlite3
from tkinter import *

#Configuracion de la raíz
root = Tk()
root.title("Bar el Wero - Menú")
root.resizable(0,0)
root.config(bd=25, relief="sunken")

Label(root, text = "   Bar el Wero   ", fg="darkblue", font=("Times New Roman",28,"bold italic")).pack()
Label(root, text = "Menú del día", fg="blue", font=("Times New Roman",24,"bold italic")).pack()

#Separación del titulo y categorías
Label(root, text="").pack()

conexion = sqlite3.connect("restaurante.db")
cursor = conexion.cursor()

# Buscar las categorias y platos de la BD
categorias = cursor.execute("SELECT * FROM categoria").fetchall()
for categoria in categorias:
    #print(categoria[1])
    Label(root, text=categoria[1], fg="black", font=("Times New Roman",20,"bold italic")).pack()
    platos = cursor.execute("SELECT * FROM plato WHERE categoria_id={}".format(categoria[0]) ).fetchall()
    for plato in platos:
        #print("\t{}".format(plato[1]) )
        Label(root, text=plato[1], fg="gray", font=("Verdana",15,"italic")).pack()
    #Separación entre categorías
    Label(root, text="").pack()

conexion.close()

Label(root, text="12$ (IVA incl.)", fg="black", font=("Times New Roman",18,"bold italic")).pack(side="right")

#Finalmente ejecutamos el bucle de la aplicación
root.mainloop()