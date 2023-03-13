# -*- coding: utf-8 -*-
"""
Created on Tue Mar 16 20:36:34 2021

@author: ENRIQUE
"""

import random
import math

def leer_numero(ini, fin, mensaje):
    while True:
        try:
            valor = int( input(mensaje) )
        except:
            print("Error: Número no válido")
        else:
            if valor>=ini and valor <=fin:
                break
    return valor


def generador():
    numeros = leer_numero(1, 20, "Cuántos números quieres generar? [1-20]")
    modo = leer_numero(1, 3, "Como quieres redondear los numeros? [1] A la alza [2]A la baja, [3]Normal")

    lista = []
    for i in range(numeros):
        numero = random.uniform(0, 101)
        if modo == 1:
            print("{} => {}".format(numero, math.ceil(numero)))
            numero = math.ceil(numero)
        elif modo ==2:
            print("{} => {}".format(numero, math.floor(numero)))
            numero = math.floor(numero)
        elif modo == 3:
            print("{} => {}".format(numero, round(numero)))
            numero = round(numero)
        lista.append(numero)
        
    return lista

generador()