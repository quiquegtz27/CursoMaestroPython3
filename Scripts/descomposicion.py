# -*- coding: utf-8 -*-
"""
Created on Wed Feb 10 20:15:43 2021

@author: ENRIQUE
"""

import sys
if len(sys.argv) == 2:
    num = int(sys.argv[1])
    if num<0 or num>9999:
        print("Introduce un número correcto")
    else:
        cad = str(num)
        long = len(cad)
        for i in range(long):
            print("{:04d}".format(int(cad[long-1-i])*10**i))
else:
    print("Error: Introduce los argumentos correctamente.")
    print("Ejemplo:python descomposicion.py [0-9999]")
        