# -*- coding: utf-8 -*-
"""
Created on Tue Aug 17 16:38:51 2021

@author: Manjuanel
"""

import csv
import sys
def costo_camion(nombre_archivo):
    with open(nombre_archivo, 'rt') as file:  #abre el archivo
            rows = csv.reader(file) #ahora lee el archivo con modulo CSV
            header = next(file) #esto para no leer la primera linea
            acumulador = 0 
    
            for row in rows:
                cajones = int(row[1])
                precio = float(row[2])
                precio_total = cajones * precio
                acumulador = precio_total + acumulador

        #print(cajones)
        #print(precio)
        #print(precio_total)
        #print(acumulador)
        
            return acumulador           #Fin de la función

if len(sys.argv) == 2:
    nombre_archivo = sys.argv[1]
else: 
    nombre_archivo: '../Data/camion.csv'

costo = (costo_camion('F:/Desktop/Ejercicios/ejercicios_python/Data/camion.csv'))
print(costo)