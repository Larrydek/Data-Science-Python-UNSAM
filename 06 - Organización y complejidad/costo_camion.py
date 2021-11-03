# -*- coding: utf-8 -*-
"""
Created on Mon Aug 16 15:50:21 2021

@author: Manjuanel
"""

import fileparse
def costo_camion(nombre_archivo):
    camion = fileparse.parse_csv(nombre_archivo_camion, select = ['nombre', 'cajones', 'precio'], types = [str, int, float], has_headers = True)
    precio_total = 0
    for x in camion:
        precio_total += x['cajones']*x['precio']
    return precio_total

nombre_archivo_camion = 'F:/Desktop/Ejercicios/ejercicios_python/Data/fecha_camion.csv'
print(costo_camion(nombre_archivo_camion))



