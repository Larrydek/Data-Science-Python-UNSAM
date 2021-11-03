# -*- coding: utf-8 -*-
"""
Created on Wed Sep  8 12:25:59 2021

@author: Manjuanel
"""
#Imports
import random
import numpy as np
import matplotlib.pyplot as plt

n_repeticiones = 100
figus_total = 670

#Ejercicio 5.10: Crear album vacío
def crear_album(figus_total):
    album = np.zeros(figus_total) #album vacío
    return album

album = crear_album(figus_total)

#Ejercicio 5.11: Definir si está completo o no
def album_incompleto(album):
    if 0 in album:
        return True
    else: 
        return False
    
#Ejercicio 5.12:  Comprar figu  
def comprar_figu(figus_total):
    figurita = random.randint(0,figus_total-1)
    return figurita


#Ejercicio 5.13: Cantidad de Compras

def cuantas_figus(figus_total):
    album = crear_album(figus_total)
    c = 0
    while album_incompleto(album):      
        figurita = comprar_figu(figus_total)
        #print(album)
        album[figurita] += 1
        c += 1
        
    #print(album)
    #print(c) #Anota la cantidad de figuritas en la lista
    
    return c

c = cuantas_figus(figus_total)
#Ejercicio 5.14/5.15:
#
lista = []
def experimento_figus(n_repeticiones, figus_total):
    for i in range(n_repeticiones):
        lista.append(cuantas_figus(figus_total)) #va metiendo en la lista el resultado de cuantas figuritas
    
    return np.mean(lista) #devuelve el promedio de esa lista


#print(cuantas_figus(figus_total))
#print(experimento_figus(n_repeticiones, figus_total))

#Ejercicio 5.17: Comprar paquete

figus_total = 670
n_repeticiones = 100
figus_paquete = 5

def comprar_paquete(figus_total, figus_paquete):
    p = []
    for i in range(figus_paquete):
        p.append(comprar_figu(figus_total))
        return p
    
#Ejercicio 5.18: Cuantos paquetes
def cuantos_paquetes(figus_total, figus_paquete):
    album = crear_album(figus_total)
    while album_incompleto(album):
        paquete = comprar_paquete(figus_total, figus_paquete)
        while paquete:
            album[paquete.pop()] += 1
    return album.sum()/figus_paquete

print(cuantos_paquetes(figus_total, figus_paquete))



lista_paquetes = []

for i in range(n_repeticiones):
    lista_paquetes.append(cuantos_paquetes(figus_total, figus_paquete))
    
print(lista_paquetes)
    
print(f'Para llenar un album de {figus_total} figus se necesitaron en promedio:{np.mean(lista_paquetes)}')

#Ejercicio 5.19: Graficar
    
def calcular_historia_figus_pegadas(figus_total, figus_paquete):
    album = crear_album(figus_total)
    historia_figus_pegadas = [0]
    while album_incompleto(album):
        paquete = comprar_paquete(figus_total, figus_paquete)
        while paquete:
            album[paquete.pop()] = 1
        figus_pegadas = (album>0).sum()
        historia_figus_pegadas.append(figus_pegadas)        
    return historia_figus_pegadas

figus_total = 670
figus_paquete = 5

plt.plot(calcular_historia_figus_pegadas(figus_total, figus_paquete))
plt.xlabel("Cantidad de paquetes comprados.")
plt.ylabel("Cantidad de figuritas pegadas.")
plt.title("La curva de llenado se desacelera al final")
plt.show()
    


#Ejercicio 5.20:Probabilidad aprox = a frequencia relativa:
# prob de que x < 850

L = np.array(lista_paquetes) #convierte lista en array para trabajar con numpy
(L<=850).sum()/n_repeticiones #probabilidad por h(x)

#Ejercicio 5.21: Histograma
    
#plt.hist(L, bins=50)


#Ejercicio 5.22: Cantidad de paquetes a comprar para tener un 90% de chances de llenar el album
np.percentile(L,90)

#Ejercicio 5.23: 



            
    