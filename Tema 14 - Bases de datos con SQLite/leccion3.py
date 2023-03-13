import sqlite3

conexion = sqlite3.connect("usuarios_autoincremental.db")
cursor = conexion.cursor()

##SELECCIÓN DE REGISTROS SEGÚN LA EDAD
# cursor.execute("SELECT * FROM usuarios WHERE edad=51")
# usuarios= cursor.fetchall()
# print(usuarios)

## MODIFICACIÓN DE UN REGISTRO SEGÚN EL DNI
#cursor.execute("UPDATE usuarios SET nombre='Hector Costa', edad=30 WHERE dni='AAAAAAA'")

##BORRAR REGISTRO SEGÚN DNI
cursor.execute("DELETE FROM usuarios WHERE dni='AAAAAAA'")

conexion.commit()
conexion.close()