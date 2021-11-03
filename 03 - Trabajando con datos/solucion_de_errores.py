# -*- coding: utf-8 -*-
"""
Created on Fri Aug 20 16:31:25 2021

@author: Manjuanel
"""
#solucion_de_errores
#ejercicios de errores en el código
#%%
#Ejercicio 3.1: Semántica
#el error era semántico debido a que el código determinaba si la última letra era a o no.
#no reconocía 'a' mayúscula
#lo solucioné borrando el while y agregando un if con las dos condiciones
def tiene_a(expresion):
    n = len(expresion)
    if 'a' in expresion or 'A' in expresion:
        return True
    else:
        return False
        

print(tiene_a('UNSAM 2020'))
print(tiene_a('abracadabra'))
print(tiene_a('La novela 1984 de George Orwell'))

#%%
#Ejercicio 3.2: Sintáxis
#Tenía múltiples errores sintácticos, agregué ':' y '=='
#No funcionaba para mayúsculas
def tiene_a(expresion):
    n = len(expresion)
    i = 0
    while i<n:
        if expresion[i] == 'a' or expresion[i] == 'A':
            return True
        i += 1
    return False

print(tiene_a('UNSAM 2020'))
print(tiene_a('La novela 1984 de George Orwell'))

#%%
#Ejercicio 3.3: Tipos
#No funcionaba para números ya que el condicional del if es '1' (string)
#transformé la variable a string para ser usada en todo el programa

def tiene_uno(expresion):
    expresion = str(expresion)
    n = len(expresion)
    i = 0
    tiene = False
    while (i<n) and not tiene:
        if expresion[i] == '1':
            tiene = True
        i += 1
    return tiene


print(tiene_uno('UNSAM 2020'))
print(tiene_uno('La novela 1984 de George Orwell'))
print(tiene_uno(1984))

#%%
#Ejercicio 3.4: Alcances
#La función nunca cerraba
#Le agregué el return a la función para que devuelva C y pueda ser usada

def suma(a,b):
    c = a + b
    return c

a = 2
b = 3
c = suma(a,b)
print(f"La suma da {a} + {b} = {c}")
print(suma(2,3))

#%%
#Ejercicio 3.5: Pisando memoria
#El problema era que siempre llenaba el registro con el último dato del camión
#Lo solucioné vaciando el registro despues de cada empuje de datos del camión al registro

import csv
from pprint import pprint

def leer_camion(nombre_archivo):
    camion=[]
    registro={}
    with open(nombre_archivo,"rt") as f:
        filas = csv.reader(f)
        encabezado = next(filas)
        for fila in filas:
            registro[encabezado[0]] = fila[0]
            registro[encabezado[1]] = int(fila[1])
            registro[encabezado[2]] = float(fila[2])
            pprint(registro)
            #pprint(camion)
            camion.append(registro)
            registro = {}
    return camion

camion = leer_camion('../Data/camion.csv')
pprint(camion)
