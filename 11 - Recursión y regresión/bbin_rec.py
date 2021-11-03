# -*- coding: utf-8 -*-
"""
Created on Wed Oct 27 12:48:51 2021

@author: Manjuanel
"""
#Ejercicio 11.11: Búsqueda binaria

def bbinaria_rec(lista, e):
    if len(lista) == 0:
        res = False
    elif len(lista) == 1:
        res = lista[0] == e     #Si el único número que queda es "e" ---> True
    else:
        medio = len(lista)//2
        res = lista[medio] == e
        if e < lista[medio]:
            res = bbinaria_rec(lista[:medio] , e) #Buscalo en la mitad izquierda
        elif e > lista[medio]:                    #(Sin incluir el medio)
            res = bbinaria_rec(lista[medio+1:], e) #Buscalo en la mitad derecha
    return res

lista = [1,2,4,5,7,15,17,18,21,24,27]
e = 9
print(bbinaria_rec(lista, e))
