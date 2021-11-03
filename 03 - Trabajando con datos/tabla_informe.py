# -*- coding: utf-8 -*-
"""
Created on Tue Aug 24 14:21:47 2021

@author: Manjuanel
"""

from pprint import pprint
import csv
def leer_camion(nombre_archivo):
    with open(nombre_archivo, 'rt') as file:  #abre el archivo
            rows = csv.reader(file) #ahora lee el archivo con modulo CSV
            header = next(rows) #esto para no leer la primera linea
            camion = []
            precio_total = 0
            
            for n_row, row in enumerate(rows, start=1): #para cada row (con indice n_row, empezando de 1) en las rows
                record = dict(zip(header, row)) #crea un objeto que tenga la lista de cada header con cada elemento de row
                #pprint(record)
                cajones = int(record['cajones']) #transforma la cadena a número entero
                precio = float(record['precio']) #transforma la cadena a número con coma
                inter = {'nombre': row[0], 'cajones': cajones , 'precio': precio} #pone los valores en diccionario
                camion.append(inter) #metelo en camion
                precio_total = precio_total + inter['precio'] * inter['cajones'] #va sumando precios
                inter = {} #vacia el intermediario
            
            return camion

            print(precio_total)
nombre_archivo = 'F:/Desktop/Ejercicios/ejercicios_python/Data/fecha_camion.csv'
camionsito = leer_camion(nombre_archivo)


def leer_precios(nombre_archivo):
    with open(nombre_archivo, 'rt') as file:
        precios = {}
        rows = csv.reader(file)
        for row in rows:
            if row == []: 
                del row
                break
            precios[row[0]] = row[1]
        return precios

    
        
nombre_archivo = 'F:/Desktop/Ejercicios/ejercicios_python/Data/precios.csv'
precios = leer_precios(nombre_archivo)
pprint('Detalles de la compra al productor: ' + str(camionsito))
pprint('Detalles de la venta: ' + str(precios))

total_verdu = 0
precio_total = 0
a = 0

while a < len(camionsito):
    total_verdu += float(precios[camionsito[a]['nombre']]) * int(camionsito[a]['cajones'])
    precio_total += int(camionsito[a]['cajones']) * float(camionsito[a]['precio'])
    
    a += 1

balance = total_verdu - precio_total
print('El costo de compra al productor fue de ' + str(precio_total) + ' y el monto de venta de esos productos fue de ' + str(total_verdu))
print('La ganancia fue de ' + str(balance))

def hacer_informes(camionsito, precios):
    camioneta = camionsito.copy()
    listón = []
    for i in range(len(camioneta)):
        camioneta[i]['cambio'] = float(precios[camioneta[i]['nombre']]) - camioneta[i]['precio']
        lista = []
        for keys in camioneta[i]:
            lista.append(camioneta[i][keys])
        
        listón.append(tuple(lista))
    #print(listón)
    return listón

print(hacer_informes(camionsito, precios))

headers = ('Nombre', 'Cajones', 'Precio', 'Cambio')
lineas = '---------- ---------- ---------- ----------'
print(f'{headers[0]:>10s} {headers[1]:>10s} {headers[2]:>10s} {headers[3]:>10s}')
print(lineas)
informe = hacer_informes(camionsito, precios)
for nombre, cajones, precio, cambio in informe:
    print(f'{nombre:>10s} {cajones:>10d} {"$":>5s}{precio:<10.2f} {cambio:<10.2f}')

        

