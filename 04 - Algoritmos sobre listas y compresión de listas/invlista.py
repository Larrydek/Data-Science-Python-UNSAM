# -*- coding: utf-8 -*-
"""
Created on Tue Aug 31 19:57:38 2021

@author: Manjuanel
"""

#%%
#Ejercicio 4.5: Invertir una lista
def invertir_lista(lista):
    revList = []
    i = len(lista) - 1          #empeza desde el final
    while i >= 0:
        revList.append(lista[i]) #empuja el valor en el nuevo array
        i = i - 1                # resta posición
    return revList

print(invertir_lista(['Bogotá', 'Rosario', 'Santiago', 'San Fernando', 'San Miguel']))
        