# -*- coding: utf-8 -*-
"""
Created on Tue Mar 16 20:26:08 2021

@author: ENRIQUE
"""

def suma(a,b):
    try:
        r = a + b
    except TypeError:
        print("Error: Tipo de dato no válido")
    else:
        return r

def resta(a,b):
    try:
        r = a - b
    except TypeError:
        print("Error: Tipo de dato no válido")
    else:
        return r 


def producto(a,b):
    try:
        r = a * b
    except TypeError:
        print("Error: Tipo de dato no válido")
    else:
        return r 


def division(a,b):
    try:
        r = a / b
    except TypeError:
        print("Error: Tipo de dato no válido")
    except ZeroDivisionError:
        print("Error: No es posible dividir por cero")
    else:
        return r 