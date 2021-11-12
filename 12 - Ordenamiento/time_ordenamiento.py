# -*- coding: utf-8 -*-
"""
Created on Tue Nov  9 18:54:13 2021

@author: Manjuanel
"""


import random
import timeit as tt
import numpy as np
import matplotlib.pyplot as plt
#%%
#ORDEN POR SELECCION

def ord_seleccion(lista):
    """Ordena una lista de elementos según el método de selección.
       Pre: los elementos de la lista deben ser comparables.
       Post: la lista está ordenada."""

    # posición final del segmento a tratar
    n = len(lista) - 1
    contador = []

    # mientras haya al menos 2 elementos para ordenar
    while n > 0:
        # posición del mayor valor del segmento
        p = buscar_max(lista, 0, n)[0]
        contador.append(buscar_max(lista, 0, n)[1])

        # intercambiar el valor que está en p con el valor que
        # está en la última posición del segmento
        lista[p], lista[n] = lista[n], lista[p]
        #print("DEBUG: ", p, n, lista)


        # reducir el segmento en 1
        n -= 1
    contador = sum(contador)
    return lista, contador

def buscar_max(lista, a, b):
    """Devuelve la posición del máximo elemento en un segmento de
       lista de elementos comparables.
       La lista no debe ser vacía.
       a y b son las posiciones inicial y final del segmento"""

    contador = 0
    pos_max = a
    for i in range(a + 1, b + 1):
        contador += 1
        if lista[i] > lista[pos_max]:
            pos_max = i
    return pos_max, contador

#%%
#ORDEN POR INSERCION

def ord_insercion(lista):
    """Ordena una lista de elementos según el método de inserción.
       Pre: los elementos de la lista deben ser comparables.
       Post: la lista está ordenada."""
    contador = []

    for i in range(len(lista) - 1):
        # Si el elemento de la posición i+1 está desordenado respecto
        # al de la posición i, reubicarlo dentro del segmento [0:i]
        contador.append(1)
        if lista[i + 1] < lista[i]:
            contador.append(reubicar(lista, i + 1))
        #print("DEBUG: ", lista)
    
    contador = sum(contador)

    return lista, contador

def reubicar(lista, p):
    """Reubica al elemento que está en la posición p de la lista
       dentro del segmento [0:p-1].
       Pre: p tiene que ser una posicion válida de lista."""

    v = lista[p]
    contador = 0

    # Recorrer el segmento [0:p-1] de derecha a izquierda hasta
    # encontrar la posición j tal que lista[j-1] <= v < lista[j].
    j = p
    while j > 0 and v < lista[j - 1]:
        # Desplazar los elementos hacia la derecha, dejando lugar
        # para insertar el elemento v donde corresponda.
        lista[j] = lista[j - 1]
        contador += 1
        j -= 1

    lista[j] = v
    
    return contador
#%%
#BURBUJEO

def ord_burbujeo(lista1):
    lista = lista1.copy()
    n = len(lista) - 1
    contador = 0

    for i in range(len(lista) - 1): #Loop que da len vueltas
        while n > 0:
            if lista[n - 1] > lista[n]:
                contador += 1
                lista = intercambiar(lista, n - 1, n)

            n -= 1
        n = len(lista) - 1     #RESETEA EL N

    return lista, contador


def intercambiar(lista, a, b):
    j = lista[b]    #valor más chico
    k = lista[a]    #valor más grande
    lista[a] = j
    lista[b] = k
    return lista
#%%
#MERGE_SORT

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
#%%
#EXPERIMENTO

def generar_lista(N):
    
    lista = []

    for i in range (N):
        i = random.randint(0,1000)
        lista.append(i)
    
    return lista

#%%

listas = []
for N in range(1, 256):
    listas.append(generar_lista(N))
    
def experimento_timeit(listas, num):
    """
    Realiza un experimento usando timeit para evaluar el método
    de selección para ordenamiento de listas
    con las listas pasadas como entrada
    y devuelve los tiempos de ejecución para cada lista
    en un vector.
    El parámetro 'listas' debe ser una lista de listas.
    El parámetro 'num' indica el número de veces que repite el ordenamiento para cada lista.
    """
    tiempos = {}
    tiempos_seleccion = []
    tiempos_burbujeo = []
    tiempos_insercion = []
    tiempos_merge = []

    global lista

    for lista in listas:

        # evalúo el método de selección
        # en una copia nueva para cada iteración
        tiempo_merge = tt.timeit('merge_sort(lista.copy())', number = num, globals = globals())
        tiempo_seleccion = tt.timeit('ord_seleccion(lista.copy())', number = num, globals = globals())
        tiempo_burbujeo = tt.timeit('ord_burbujeo(lista.copy())', number = num, globals = globals())
        tiempo_insercion = tt.timeit('ord_insercion(lista.copy())', number = num, globals = globals())

        # guardo el resultado
        tiempos_seleccion.append(tiempo_seleccion)
        tiempos_burbujeo.append(tiempo_burbujeo)
        tiempos_insercion.append(tiempo_insercion)
        tiempos_merge.append(tiempo_merge)

    # paso los tiempos a arrays
    tiempos_seleccion = np.array(tiempos_seleccion)
    tiempos_burbujeo = np.array(tiempos_burbujeo)
    tiempos_insercion = np.array(tiempos_insercion)
    tiempos_merge = np.array(tiempos_merge)
    
    tiempos['tiempos insercion']= tiempos_insercion
    tiempos['tiempos seleccion']= tiempos_seleccion
    tiempos['tiempos burbujeo']= tiempos_burbujeo
    tiempos['tiempos merge']= tiempos_merge
    
    return tiempos

tiempos = experimento_timeit(listas, 100)
plt.plot(tiempos['tiempos insercion'], label = "Insercion")
plt.plot(tiempos['tiempos seleccion'], label = "Seleccion")
plt.plot(tiempos['tiempos burbujeo'], label = "Burbujeo")
plt.plot(tiempos['tiempos merge'], label = "Merge")
plt.legend()