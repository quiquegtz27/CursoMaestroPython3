# -*- coding: utf-8 -*-
"""
Created on Wed Feb 10 20:02:52 2021

@author: ENRIQUE
"""

import sys
if len(sys.argv) == 3 and int(sys.argv[1])>0 and int(sys.argv[2])>0 and int(sys.argv[1])<9 and int(sys.argv[2])<9: 
    filas = int(sys.argv[1])
    col = int(sys.argv[2])
    
    
    for i in range(filas):
        for j in range(col):
             print(" * ", end='')
        print("")
else:
    print("Error: Introduce los argumentos correctamente.")
    print("Ejemplo: tabla.py 7 5")
        