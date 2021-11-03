# -*- coding: utf-8 -*-
"""
Created on Tue Sep 14 13:24:09 2021

@author: Manjuanel
"""

import csv

def parse_csv(f, select = None, types = None, has_headers = True, silence_errors = False):
    '''
    Parsea un archivo CSV en una lista de registros
    '''
    #with open(nombre_archivo) as f:
    rows = csv.reader(f)

    # Lee los encabezados
    if has_headers: #SI HAY ENCABEZADOS
        headers = next(rows)
        
        #Cambia el indice segun hay select
        if select: #si no es None
            try:
                indices = [headers.index(nombre_columna) for nombre_columna in select] #El indice es la posicion de los nombres del Select
                headers = select
            except ValueError as e:
                print('Falle porque:',e)
                
        else:
            indices = []
    else:
        indices = []
        if select and silence_errors == False:      #SI NO HAY ENCABEZADOS, NO PUEDE HABER SELECT!
                raise RuntimeError("Para seleccionar, necesito encabezados")
        
    registros = []
    for row in rows:
        if not row:    # Saltea filas sin datos
            continue
        
        #Cambia las filas según el indice

        if indices:
            row = [row[index] for index in indices]
        #else:
             #continue #SIGUE EL ERROR
            
        if types:
            try:
                row = [func(val) for func, val in zip(types, row)] #Aplicale la función [type] al valor que haya en la columna
            except ValueError as e:
                if not silence_errors: # MOSTRAME LOS ERRORES
                    print(f'No se pudo convertir {row}')
                    print(e)
                
            
        if not has_headers:
        #Arma tuplas con esos valores
            registro = (row[0],row[1])
            registros.append(registro)
            
        else:    
        #Armar diccionario
            registro = dict(zip(headers, row)) 
            registros.append(registro)

    return registros

#PRUEBAS CON CAMION:
#with open('../Data/camion.csv') as f:
#    camion = parse_csv(f, types = [str, int, float], silence_errors = False)
#    print('------------------------------------')
#    print(camion)

#PRUEBAS CON PRECIOS:    
#with open('../Data/precios.csv') as f:
#    precios = parse_csv(f, types = [str, float], has_headers = False, silence_errors = False)
#    print('------------------------------------')
#    print(precios)


#camion_prueba = parse_csv('../Data/camion.csv', types=[str,int,float])
#print(camion_prueba)