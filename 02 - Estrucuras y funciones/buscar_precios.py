# -*- coding: utf-8 -*-
"""
Created on Mon Aug 16 17:01:29 2021

@author: Manjuanel
"""

def buscar_precio(fruta):
    
    encuentra = 0
    
    with open('../Data/precios.csv', 'rt') as file: #abrir archivo sin necesidad de cerrar
        
        for line in file:           #para cada linea en el archivo
            row = line.split(',')   #separar datos
            
            if row[0] == fruta:     #si esta la fruta
                encuentra = 1       #si encontró la fruta = 1
                return 'El precio de la ' + fruta + ' es ' + row[1]  #dame el precio
                
        if encuentra == 0:          #si no encontró tu fruta
            return 'No hay stock de ' + fruta
            
print(buscar_precio('Naranja'))