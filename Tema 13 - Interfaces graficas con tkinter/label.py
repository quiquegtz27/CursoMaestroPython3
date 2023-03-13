from tkinter import *

root = Tk()
'''
#Variables dinámicas
texto = StringVar()
texto.set("Un nuevo texto")

Label(root, text="Hola mundo").pack(anchor="nw") #nw NorthWest
label = Label(root,text="Otra etiqueta")
label.pack(anchor="center")
Label(root, text="Ultima etiqueta").pack(anchor="se")

label.config(bg="green", fg="blue", font=("Verdana",24))
label.config(textvariable=texto)
'''

imagen = PhotoImage(file="imagen.gif")
Label(root, image=imagen, bd=0).pack(side="left")

#Abajo del todo
#Es el bucle de la aplicación
root. mainloop()