import sqlite3 ##Importando el modulo

#Conexión a la BD // se crea la BD si no existe
conexion = sqlite3.connect("ejemplo.db")

#Creación del cursor para realizar las consultas
cursor = conexion.cursor()

#Ejecutar código en SQL para crear las tablas
#cursor.execute(
 #   "CREATE TABLE usuarios (nombre VARCHAR(100), edad INTEGER, email VARCHAR(100) )")

#Insrtar un nuevo usuario
#cursor.execute(
#    "INSERT INTO usuarios VALUES ('Héctor', 27, 'hector@ejemplo.com')")

##Consulta para recuperar el registro
#cursor.execute("SELECT * FROM usuarios")
#usuario = cursor.fetchone()
#print(usuario[0], usuario[1])

##Insrtar varios usuarios de una
#usuarios = [
#        ('Mario',51,'mario@ejemplo.com'),
#        ('Mercedes',38,'mercedes@ejemplo.com'),
#        ('Juan',19,'juan@ejemplo.com')
#    ]
#cursor.executemany("INSERT INTO usuarios VALUES (?,?,?)", usuarios)

#Recuperar varios registros
cursor.execute("SELECT * FROM usuarios")
usuarios = cursor.fetchall()
for usuario in usuarios:
    print("Nombre: ",usuario[0], " - email: ", usuario[2])

conexion.commit()
conexion.close()
