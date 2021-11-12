# -*- coding: utf-8 -*-
"""
Created on Thu Nov  4 10:55:45 2021

@author: Manjuanel
"""

def ord_burbujeo(lista1):
    lista = lista1.copy()
    n = len(lista) - 1
    
    for i in range(len(lista) - 1): #Loop que da len vueltas
        while n > 0:
            if lista[n - 1] > lista[n]:
                lista = intercambiar(lista, n - 1, n)
                
            n -= 1
        n = len(lista) - 1     #RESETEA EL N
    
    return lista
                        
        
def intercambiar(lista, a, b):
    j = lista[b]    #valor más chico
    k = lista[a]    #valor más grande
    lista[a] = j
    lista[b] = k
    return lista

#lista_1 = [1, 2, -3, 8, 1, 5]
lista_3 = [0, 9, 3, 8, 5, 3, 2, 4]

#burbujita = ord_burbujeo(lista_1)
burbuja3 = ord_burbujeo(lista_3)

lista_4 = [10, 8, 6, 2, -2, -5]
burbuja4 = ord_burbujeo(lista_4)
    