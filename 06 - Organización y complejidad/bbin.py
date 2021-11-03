# -*- coding: utf-8 -*-
"""
Created on Tue Sep 14 23:35:59 2021

@author: Manjuanel
"""
#EJERCICIO 6.15: 
def donde_insertar(lista, x, verbose = False):
    '''Búsqueda binaria
    DEVUELVE LA POSICIÓN EN DONDE HUBIESE IDO EL ELEMENTO,
    PERO NO CAMBIA LA LISTA ORIGINAL
    '''
    listaFinal = lista[:] #CREAMOS UNA COPIA DE LA LISTA PARA NO MODIFICAR LA LISTA ORIGINAL
    lista.sort()
    if verbose:
        print(f'[DEBUG] izq |der |medio')
    pos = -1 # Inicializo respuesta, el valor no fue encontrado
    izq = 0
    der = len(lista) - 1
    while izq <= der:
        medio = (izq + der) // 2
        if verbose:
            print(f'[DEBUG] {izq:3d} |{der:>3d} |{medio:3d}')
        if lista[medio] == x:
            pos = medio     # elemento encontrado!
            break
        if lista[medio] > x:
            der = medio - 1 # descarto mitad derecha
        else:               # if lista[medio] < x:
            izq = medio + 1 # descarto mitad izquierda
        
    #SI NO ESTÁ EL ELEMENTO
    if pos == -1: 
        listaFinal.append(x) #METELO
        listaFinal.sort() #ordena la lista
        pos = listaFinal.index(x) #dame la posición
        print(lista)
        print(listaFinal)
        return pos
    #SI ESTABA, DEVOLVE LA POSICIÓN
    else:
        return pos
    
def insertar(lista, x, verbose = False):
    '''Búsqueda binaria
    TE DICE EN QUE POSICIÓN ESTÁ X NUMERO,
    SI NO ESTÁ
    METE EN LA LISTA UN NÚMERO Y DEVUELVE LA POSICIÓN
    '''
    lista.sort()
    if verbose:
        print(f'[DEBUG] izq |der |medio')
    pos = -1 # Inicializo respuesta, el valor no fue encontrado
    izq = 0
    der = len(lista) - 1
    while izq <= der:
        medio = (izq + der) // 2
        if verbose:
            print(f'[DEBUG] {izq:3d} |{der:>3d} |{medio:3d}')
        if lista[medio] == x:
            pos = medio     # elemento encontrado!
            break
        if lista[medio] > x:
            der = medio - 1 # descarto mitad derecha
        else:               # if lista[medio] < x:
            izq = medio + 1 # descarto mitad izquierda
        
    #SI NO ESTÁ EL ELEMENTO
    if pos == -1: 
        lista.append(x) #METELO
        lista.sort() #ordena la lista
        pos = lista.index(x) #dame la posición
        print(lista)
        return pos
    #SI ESTABA, DEVOLVE LA POSICIÓN
    else:
        return pos
    


print(donde_insertar([0,1,2,5,8,9,11,15,17,18], 3, verbose = True))
