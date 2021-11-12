# -*- coding: utf-8 -*-
"""
Created on Mon Nov  8 12:20:25 2021

@author: Manjuanel
"""
import random

def generar_lista(N):
    lista = []
    
    for i in range(N):
        i = random.randint(0,1000)
        lista.append(i)
    return lista

#generar_lista(85)

#%%
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
    
    return contador
                        
        
def intercambiar(lista, a, b):
    j = lista[b]    #valor más chico
    k = lista[a]    #valor más grande
    lista[a] = j
    lista[b] = k
    return lista

#ord_burbujeo(generar_lista(41))
#lista = [5, 4, 3, 2, 1]
#ord_burbujeo(lista)
#%%
#ORDENAMIENTO INSERCIÓN
def ord_insercion(lista):
    """Ordena una lista de elementos según el método de inserción.
       Pre: los elementos de la lista deben ser comparables.
       Post: la lista está ordenada."""
    contador = 0
    
    for i in range(len(lista) - 1):
        # Si el elemento de la posición i+1 está desordenado respecto
        # al de la posición i, reubicarlo dentro del segmento [0:i]
        contador += 1
        if lista[i + 1] < lista[i]:
            #reubicar(lista, i + 1)
            contador += reubicar(lista, i + 1)
        #print("DEBUG: ", lista)
    
    #contador = sum(contador)

    return lista, contador

def reubicar(lista, p):
    """Reubica al elemento que está en la posición p de la lista
       dentro del segmento [0:p-1].
       Pre: p tiene que ser una posicion válida de lista."""
    contador = 0
    v = lista[p]

    # Recorrer el segmento [0:p-1] de derecha a izquierda hasta
    # encontrar la posición j tal que lista[j-1] <= v < lista[j].
    j = p
    while j > 0 and v < lista[j - 1]:
        # Desplazar los elementos hacia la derecha, dejando lugar
        # para insertar el elemento v donde corresponda.
        contador += 1
        lista[j] = lista[j - 1]
        j -= 1

    lista[j] = v
    
    return contador
    
#lista = [3, 2, -1, 2, 0, 5]
#ord_insercion(lista)
#ord_insercion([2, 3, -1, 5, 0, 2])
#ord_insercion([1,2,3,4,5,6,7,8])

#%%
#ORDENAMIENTO SELECCIÓN

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

def buscar_max(lista, a, b, contador = 0):
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

#lista = [3, 2, -1, 5, 0, 2]
#ord_seleccion(lista)

#%%
#Merge-sort
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
#EXPERIMENTOS

def experimento(N, k):
    B = []
    I = []
    S = []
    M = []
    
    for i in range(k):
        lista = generar_lista(N)
        B.append(ord_burbujeo(lista.copy()))
        I.append(ord_insercion(lista.copy())[1])
        S.append(ord_seleccion(lista.copy())[1])
        M.append(merge_sort(lista.copy())[1])
        
    B = sum(B)/k
    I = sum(I)/k
    S = sum(S)/k
    M = sum(M)/k
    
    return (B,I,S,M)

    
    
experimento(10, 2)
experimento(5, 1000)
experimento(50, 10)

    