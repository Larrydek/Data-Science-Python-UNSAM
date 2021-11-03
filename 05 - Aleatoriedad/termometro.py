# -*- coding: utf-8 -*-
"""
Created on Tue Sep  7 19:03:48 2021

@author: Manjuanel
"""
import random
import numpy as np


def medir_temp(N):
    mediciones = []
    real = 37.5
    
    #anotar N mediciones
    i = 0
    while i < N:
        error = random.normalvariate(0,0.2) #error con Mu 0 y Sigma 0.2
        medida = real + error 
        mediciones.append(medida)   #empujalo a la lista
        i += 1
    
    mediciones = np.array([mediciones]) #ARMA UN VECTOR
        
    return mediciones

N = 999
mediciones = medir_temp(N)
np.save('../Data/temperaturas.npy', mediciones) #GUARDA LAS MEDICIONES EN UN .NPY
np.savetxt('../Data/temperaturas.csv', mediciones)

print(mediciones)

def resumen_temp(mediciones):
    max = np.max(mediciones)
    min = np.min(mediciones)
    mean = np.mean(mediciones)
    mediana = np.sort(mediciones)[0,448] #ordeno las mediciones y elijo la de la posición del medio 999/2
    return max,min,mean,mediana

print(resumen_temp(mediciones))
    

    