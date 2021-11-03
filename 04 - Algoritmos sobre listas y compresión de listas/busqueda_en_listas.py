# -*- coding: utf-8 -*-
"""
Created on Tue Aug 31 03:53:44 2021

@author: Manjuanel
"""
#%%
#Encuentra la última posición de x
def buscar_u_elemento(lista, e):
    pos = len(lista) - 1
    while pos >= 0 and lista[pos] != e:
        pos -= 1
    return pos
print(buscar_u_elemento([1,2,3,2,3,4],3))


#Cuenta la cantidad de veces que x aparece
def buscar_n_elementos(lista, x):
    c = 0
    
    for a in lista:
        if a == x:
            c = c + 1
    return c

print(buscar_n_elementos([1,2,3,2,3,4], 3))

#%%
#Ejercicio 4.4: Máximo
def maximo(lista):
    '''Devuelve el máximo de una lista, 
    la lista debe ser no vacía y de números positivos.
    '''
    # m guarda el máximo de los elementos a medida que recorro la lista. 
    m = lista[0]    #Inicializo m como el primer valor de la lista
    for e in lista: # Recorro la lista
        if e > m:   # si el elemento es mayor al máximo hasta ahora
            m = e   # el máximo es el nuevo elemento
    return m

print(maximo([-5,-4]))

#Calculo del mínimo
def minimo(lista):
    m = lista[0]
    for e in lista:
        if e < m:
            m = e
    return m

print(minimo([-5,-4]))


        
        
    