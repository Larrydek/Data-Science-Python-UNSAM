# -*- coding: utf-8 -*-
"""
Created on Tue Sep 14 13:24:09 2021

@author: Manjuanel
"""

import csv

def parse_csv(nombre_archivo, select = None, types = None, has_headers = True):
    '''
    Parsea un archivo CSV en una lista de registros
    '''
    with open(nombre_archivo) as f:
        rows = csv.reader(f)

        # Lee los encabezados
        if has_headers:
            headers = next(rows)
            
            #Cambia el indice segun hay select
            if select: #si no es None
                indices = [headers.index(nombre_columna) for nombre_columna in select] #El indice es la posicion de los nombres del Select
                headers = select
            else:
                indices = []
        else:
            indices = []
            
        registros = []
        for row in rows:
            if not row:    # Saltea filas sin datos
                continue
            
            #Cambia las filas según el indice
            if indices:
                row = [row[index] for index in indices]
                
            if types:
                row = [func(val) for func, val in zip(types, row)] #Aplicale la función [type] al valor que haya en la columna
                
            if not has_headers:
            #Arma tuplas con esos valores
                registro = (row[0],row[1])
                registros.append(registro)
                
            else:    
            #Armar diccionario
                registro = dict(zip(headers, row)) 
                registros.append(registro)

    return registros

camion = parse_csv('../Data/camion.csv', select = ['nombre','cajones'])
print(camion)


cajones_lote = parse_csv('../Data/precios.csv', types=[str, float], has_headers=False)
print(cajones_lote)
