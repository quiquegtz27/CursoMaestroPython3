from tkinter import *

root = Tk()

root.title("Hola mundo")
root.resizable(1,1) ## (X,Y) --> X->Hor, Y->Ver
root.iconbitmap('hola.ico')

#Creación del frame en la raíz
frame = Frame(root)
#Que se empaque dentro de root
frame.pack(fill='both', expand=1)  #(side="bottom", anchor="w")
#Estableciendo las dimensiones de la ventana
frame.config(width=480, height=320)
#Configurar un cursor
frame.config(cursor="pirate")
#Configurando el color de fondo
frame.config(bg="lightblue")
#configurando el borde
frame.config(bd=25)
frame.config(relief="sunken")

#Configurando ahora la raíz
root.config(cursor="arrow")
root.config(bg="blue")
root.config(bd=15)
root.config(relief="ridge")


#Abajo del todo
#Es el bucle de la aplicación
root. mainloop()