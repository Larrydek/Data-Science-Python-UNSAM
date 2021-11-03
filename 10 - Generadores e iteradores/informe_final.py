#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# informe_final.py

#%% ejercicio 7.7
import fileparse
import lote
import formato_tabla

from camion import Camion

def leer_camion(nombre_archivo):
    '''
    Computa el precio total del camion (cajones * precio) de un archivo
    '''
    with open(nombre_archivo) as f:
        camion_dicts = fileparse.parse_csv(f, select = ['nombre', 'cajones', 'precio'], types = [str, int, float])
        camion = [lote.Lote(d['nombre'], d['cajones'], d['precio']) for d in camion_dicts]
    return Camion(camion)


def leer_precios(nombre_archivo):
    with open(nombre_archivo) as f:
        precios = fileparse.parse_csv(f, types = [str, float], has_headers = False)
    return precios


def hacer_informe(camion, precios):
    lista = []
    for x in camion:
        cambio = precios[x.nombre] - x.precio
        t = (x.nombre, x.cajones, x.precio, cambio) #ahora hecho para objetos
        lista.append(t)
    return lista


def imprimir_informe(data_informe, formateador):
    '''
    IMPRIME UNA TABLA PROLIJA desde una LISTA de TUPLAS
    con (nombre, cajones, precio, diferencia)

    '''
    formateador.encabezado(['Nombre','Cantidad','Precio','Cambio'])
    for nombre, cajones, precio, cambio in data_informe:
        rowdata = [nombre, str(cajones), f'${precio:0.2f}', f'${cambio:0.2f}']
        formateador.fila(rowdata)
        

def informe_camion(archivo_camion, archivo_precios, fmt = 'txt'):
    '''
    Crea un INFORME a partir de un archivo de CAMIÓN
    y otro de PRECIOS de venta
    El formato predeterminado es .Texto
    Alternativas: .HTML y .CSV
    '''
    #Leer archivos con datos
    camion = leer_camion(archivo_camion)
    precios = dict(leer_precios(archivo_precios))
    
    #Crear los datos para el informe
    data_informe = hacer_informe(camion, precios)    
    
    #FORMATOS
    formateador = formato_tabla.crear_formateador(fmt) #Elige el formato
    imprimir_informe(data_informe, formateador)

#PRUEBA:    
#informe_camion('../Data/camion.csv', '../Data/precios.csv', fmt = 'txt')
    

#%%
def f_principal(argumentos):
    try:
        informe_camion(argumentos[1], argumentos[2], argumentos[3]) #Intentá agarrar 3 argumentos
    except IndexError:                                              #si hay menos
        informe_camion(argumentos[1], argumentos[2])          #Intentá con menos


if __name__ == '__main__':
    import sys
    f_principal(sys.argv)

