import sqlite3

conexion = sqlite3.connect("usuarios_autoincremental.db")
cursor = conexion.cursor()

#CREACIÓN DE UNA LLAVE ÚNICA
# cursor.execute('''
#        CREATE TABLE usuarios (
#            dni VARCHAR(9) PRIMARY KEY,
#            nombre VARCHAR(100),
#            edad INTEGER,
#            email VARCHAR(100)
#            )
#            ''')

# usuarios = [
#         ('AAAAAAA','Hector',27,'hector@ejemplo.com'),
#         ('BBBBBBB','Mario',51,'mario@ejemplo.com'),
#         ('CCCCCCC','Mercedes',38,'mercedes@ejemplo.com'),
#         ('DDDDDDD','Juan',19,'juan@ejemplo.com')
#     ]
# cursor.executemany("INSERT INTO usuarios VALUES (?,?,?,?)", usuarios)

#CAMPOS AUTOINCREMENTALES
# cursor.execute(''' 
#          CREATE TABLE productos (
#              id INTEGER PRIMARY KEY AUTOINCREMENT,
#              nombre VARCHAR(100) NOT NULL,
#              marca VARCHAR(50) NOT NULL,
#              precio FLOAT NOT NULL
#              )
#                ''')

# productos = [
#     ('Teclado','Logitech',19.95),
#     ('Pantalla 19"', 'LG', 89.95)
#     ]

# cursor.executemany("INSERT INTO productos VALUES (null,?,?,?)", productos)

#CLAVES ÚNICAS: CAMPOS NO REPETIBLES A PARTE DE LAS CLAVES PRIMARIAS
cursor.execute(''' 
           CREATE TABLE usuarios(
               id INTEGER PRIMARY KEY AUTOINCREMENT,
               dni VARCHAR(9) UNIQUE,
               nombre VARCHAR(100),
               edad INTEGER,
               email VARCHAR(100)
               )
               ''')
usuarios = [
        ('AAAAAAA','Hector',27,'hector@ejemplo.com'),
        ('BBBBBBB','Mario',51,'mario@ejemplo.com'),
        ('CCCCCCC','Mercedes',38,'mercedes@ejemplo.com'),
        ('DDDDDDD','Juan',19,'juan@ejemplo.com')
    ]
cursor.executemany("INSERT INTO usuarios VALUES (null,?,?,?,?)", usuarios)


conexion.commit()
conexion.close()