from tkinter import *
from tkinter import messagebox as MessageBox
from tkinter import colorchooser as ColorChooser
from tkinter import filedialog as FileDialog

#Config de la raíz
root = Tk()

def test():
    #MessageBox.showinfo("Hola","Hola mundo")
    #MessageBox.showwarning("Alerta","Solo para administradores")
    #MessageBox.showerror("Error","Ha ocurrido un error inesperado")
    #resultado = MessageBox.askquestion("Salir","Estás seguro que quieres salir sin guardar?")
    #if resultado == "yes":
    #    root.destroy()
    #resultado = MessageBox.askokcancel("Salir","Sobreeescribir el fichero actual?")
    #if resultado:
    #   root.destroy()
    #resultado = MessageBox.askyesno("Salir","Estás seguro que quieres salir sin guardar?")
    #if resultado:
    #    root.destroy()
    #resultado = MessageBox.askretrycancel("Reintentar","No se puede conectar")
    #if resultado:
    #    root.destroy()
    
    ##----------------------AVANZADOS-----------------------------
    
    #ruta = FileDialog.askopenfilename(title="Abre un fichero", initialdir="C:/",
    #                                  filetypes=(("Ficheros de textos","*.txt"),
    #                                             ("Ficheros de textos avanzado","*.txt2"),
    #                                             ("Todos los ficheros","*.*")) )
    ##Este devuelve un string con la ruta completa
        
    fichero = FileDialog.asksaveasfile(title="Guardar un fichero", mode="a+", defaultextension=".txt")
    if fichero is not None:
        fichero.write("Hola!")
        fichero.close()
    ##por default equivale a open('ruta','w')
    
    #color = ColorChooser.askcolor(title="elige un color")
    ##Esta devuelve 1 tupla1 ---> ((R, G, B), #HEX)
    
    

Button(root, text="Clícame", command=test).pack()

#Loop de la app
root.mainloop()