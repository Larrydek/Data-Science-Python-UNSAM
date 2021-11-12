# -*- coding: utf-8 -*-
"""
Created on Mon Nov  8 10:34:45 2021

@author: Manjuanel
"""

import random

def merge_sort(lista):
    """Ordena lista mediante el método merge sort.
       Pre: lista debe contener elementos comparables.
       Devuelve: una nueva lista ordenada."""
    contador = 0

    if len(lista) < 2:
        lista_nueva = lista
        contador = 1
    else:
        medio = len(lista) // 2
        izq = merge_sort(lista[:medio])[0]
        contador += merge_sort(lista[:medio])[1]
        der = merge_sort(lista[medio:])[0]
        contador += merge_sort(lista[medio:])[1]
        lista_y_contador = merge(izq, der)
        lista_nueva = lista_y_contador[0]
        contador += lista_y_contador[1]
    return lista_nueva, contador

def merge(lista1, lista2):
    """Intercala los elementos de lista1 y lista2 de forma ordenada.
       Pre: lista1 y lista2 deben estar ordenadas.
       Devuelve: una lista con los elementos de lista1 y lista2."""

    c = 0 #counter

    i, j = 0, 0
    resultado = []

    while(i < len(lista1) and j < len(lista2)):
        c += 1
        if (lista1[i] < lista2[j]):
            resultado.append(lista1[i])
            i += 1
        else:
            resultado.append(lista2[j])
            j += 1

    # Agregar lo que falta de una lista
    resultado += lista1[i:]
    resultado += lista2[j:]

    return resultado, c

lista = []

for i in range (1000):
    i = random.randint(0,1000)
    lista.append(i)

lista = merge_sort(lista)

lista = [4,2,5,7,3]

merge_sort(lista)
