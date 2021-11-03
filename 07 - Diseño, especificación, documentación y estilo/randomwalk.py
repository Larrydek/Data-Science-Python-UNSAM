# -*- coding: utf-8 -*-
"""
Created on Mon Sep 27 18:25:42 2021

@author: Manjuanel
"""

import numpy as np
import matplotlib.pyplot as plt

#Caminata
def randomwalk(largo):
    pasos = np.random.randint(-1,2,largo)    
    return pasos.cumsum()


#repetidor:
def repetir(repeticiones, N):
    
    distMax = -1    #Para comenzar la variable
    distMin = N + 1 #Asegurarse de que sea mayor al primer dist
    resultadoRepeticiones = []
    fig = plt.figure() #UNA SOLA FIGURA
    
    for i in range(repeticiones):
        caminata = randomwalk(N)   #llama a randomwalk
        dist = max(abs(caminata))
        
        if dist > distMax:
            masLejano = caminata
            distMax = dist #MAXIMO MÁS GRANDE
            
        if dist < distMin:
            masCercano = caminata
            distMin = dist #MAXIMO MÁS CHICO
        
        
    
        plt.subplot(2, 1, 1) # define la figura de arriba
        plt.plot(caminata, label="Caminatas") # dibuja la curva
        plt.title("Caminatas")
        plt.xlabel('Tiempo')
        plt.ylabel('Distancia al origen')
        plt.xticks([]) # saca las marcas
        
    plt.subplot(2, 2, 3) # IMAGINA GRILLA 2 DE LARGO 3 DE ALTO. DIBUJA LA NUMERO 4
    plt.plot(masLejano)
    plt.title("Caminata más lejana")
    plt.xlabel('Tiempo')
    plt.ylabel('Distancia al origen')
    plt.xticks([])
    plt.ylim(-900, 900)
    
    plt.subplot(2, 2, 4) # MISMA GRILLA DE ARRIBA. SELECCIONA NUMERO 6
    plt.plot(masCercano)
    plt.title("Caminata más cercana")
    plt.xlabel('Tiempo')
    plt.xticks([])
    plt.yticks([])
    plt.ylim(-900, 900)


    plt.show()

        
    return masLejano, masCercano, resultadoRepeticiones
        
      
N = 100000 #pasos
repeticiones = 12
repetir(repeticiones, N)
