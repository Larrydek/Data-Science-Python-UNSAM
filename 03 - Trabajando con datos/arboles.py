# -*- coding: utf-8 -*-
"""
Created on Wed Aug 25 12:11:53 2021

@author: Manjuanel
"""
import csv
import os
import numpy as np
import matplotlib.pyplot as plt

#Ejercicio 3.18:

def leer_parque(nombre_archivo, parque):    
    with open(nombre_archivo, encoding = 'UTF-8') as file:
        arboles = csv.reader(file)
        header = next(arboles)
        camion = []
        for arbol in arboles:
            if parque in arbol:
                lote = dict(zip(header, arbol))
                camion.append(lote)
                lote = {}
        return camion

nombre_archivo = 'F:/Desktop/Ejercicios/ejercicios_python/Data/arbolado-en-espacios-verdes.csv'
parque = 'GENERAL PAZ'
arboles = leer_parque(nombre_archivo, parque)
#print(arboles)

#Ejercicio 3.19:

def especies(arboles):
    listita = []
    for n in arboles:
        listita.append(n['nombre_com'])
        especies = set(listita)
    return especies

conj_especies = especies(arboles)
#print(conj_especies)

#%%
#Ejercicio: 4.16 - 1.17
#La función devuelve una lista de diccionarios con todos los árboles
def leer_arboles(nombre_archivo):    
    with open(nombre_archivo, encoding = 'UTF-8') as file:
        arboles = csv.reader(file)
        header = next(arboles)
        arboleda = []
        for arbol in arboles:           #itera en cada linea dentro del archivo
                lote = dict(zip(header, arbol)) 
                arboleda.append(lote)
                lote = {}
        return arboleda

nombre_archivo = 'F:/Desktop/Ejercicios/ejercicios_python/Data/arbolado-en-espacios-verdes.csv'
arboleda = leer_arboles(nombre_archivo)

nombre_arbol = 'Jacarandá'  #Nombre de la especie que queramos buscar info
#Arma una tupla doble con la altura y el diametro del arbol
H=[(float(arbol['altura_tot']), float(arbol['diametro'])) for arbol in arboleda if arbol['nombre_com'] == nombre_arbol]

print(H)

#Ejercicio: 5.25: Histograma de altos de Jacarandá
fig1 = plt.figure()
os.path.join('..', 'Data', 'arbolado-en-espacios-verdes.csv')
arboleda = leer_arboles(nombre_archivo)
altos = [float(arbol['altura_tot']) for arbol in arboleda if arbol['nombre_com'] == nombre_arbol]
print(altos)
h = np.array(altos)
plt.hist(altos,bins=50)

d = np.array([float(arbol['diametro']) for arbol in arboleda if arbol['nombre_com'] == nombre_arbol])


#Ejercicio 5.26: Diametro vs Alto
def scatter_hd(H):
    plt.xlabel("diametro (cm)")
    plt.ylabel("alto (m)")
    plt.title("Relación diámetro-alto para Jacarandás")
    return plt.scatter(d,h)

fig2 = plt.figure()
scatter_hd(H)
    
    

    