from tkinter import *
'''
def hola():
    print("Hola mundo")

def crear_lbl():
    Label(root, text="Label creada dinámicamente").pack()
'''
def sumar():
    r.set( float(n1.get()) + float(n2.get()) )
    borrar()
    
def borrar():
    n1.set("")
    n2.set("")

#Configuración de la raíz
root = Tk()
root.config(bd=15)

#Button(root, text="Clic aquí", command=crear_lbl).pack()

n1 = StringVar()
n2 = StringVar()
r = StringVar()

Label(root, text="Número 1").pack()
Entry(root, justify="center", textvariable=n1).pack() #primer num
Label(root, text="Número 2").pack()
Entry(root, justify="center", textvariable=n2).pack() #segundo num

Button(root, text="Sumar", command=sumar).pack()
Label(root, text="Resultado").pack()
Entry(root, justify="center", textvariable=r, state="disable").pack() #Resultado



#El bucle de la aplicación
root.mainloop()