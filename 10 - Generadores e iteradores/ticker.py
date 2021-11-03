# -*- coding: utf-8 -*-
"""
Created on Mon Oct 25 15:02:36 2021

@author: Manjuanel
"""
#EJERCICIO 10.10: #ticker.py
#IMPORTS:
from vigilante import vigilar
import csv
import informe_final


def cambiar_tipo(rows, types):
    for row in rows:
        yield [func(val) for func, val in zip(types, row)] #Termina haciendo str(row), int(row), float(row)
        
def hace_dicts(rows, headers):
    for row in rows:
        yield dict(zip(headers, row))
        
def elegir_columnas(rows, indices):
    for row in rows:
        yield [row[index] for index in indices]

def parsear_datos(lines):
    rows = csv.reader(lines)
    rows = elegir_columnas(rows, [0, 1, 2]) #Acá las selecciona
    rows = cambiar_tipo(rows, [str, float, int])
    rows = hace_dicts(rows, ['nombre','precio','volumen'])
    return rows

def filtrar_datos(filas, nombres):
    filas = (fila for fila in filas if fila['nombre'] in nombres)
    return filas
            
def imprimir_ticker(data, formateador):
    rowdata = [data['nombre'], '$'+str(data['precio']), str(data['volumen'])] 
    formateador.fila(rowdata)
    
def ticker(camion_file, log_file, fmt = 'txt'):
    from formato_tabla import crear_formateador
    
    camion = informe_final.leer_camion(camion_file)
    rows = parsear_datos(vigilar(log_file))
    rows = filtrar_datos(rows, camion)
    
    formateador = crear_formateador(fmt)
    formateador.encabezado(['Nombre', 'Precio', 'Volumen'])
    
    for row in rows:
        imprimir_ticker(row, formateador)
        
#PRUEBAS:
#ticker('../Data/camion.csv', '../Data/mercadolog.csv', 'txt')
            

        

