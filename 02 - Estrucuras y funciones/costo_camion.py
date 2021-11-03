# -*- coding: utf-8 -*-
"""
Created on Mon Aug 16 15:50:21 2021

@author: Manjuanel
"""

import csv
def costo_camion(nombre_archivo):
    with open(nombre_archivo, 'rt') as file:  #abre el archivo
            rows = csv.reader(file) #ahora lee el archivo con modulo CSV
            header = next(rows) #esto para no leer la primera linea
            #print(header)
            precio_total = 0 
    
            for n_row, row in enumerate(rows, start=1):
                record = dict(zip(header, row))
                #print(record)
                try:
                    cajones = int(record['cajones'])
                    precio = float(record['precio'])
                    precio_total += cajones * precio
                    
                except ValueError: 
                    print(f'Fila {n_row}: No se puede interpretar: {row}' )

        #print(cajones)
        #print(precio)
        #print(precio_total)
            
        
            return precio_total
costo_camion('F:/Desktop/Ejercicios/ejercicios_python/Data/fecha_camion.csv')

