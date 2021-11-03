# -*- coding: utf-8 -*-
"""
Created on Tue Aug 17 18:05:19 2021

@author: Manjuanel
"""
def gering(lista):
    #lista = ['banana', 'manzana', 'mandarina'] #palabras normales
    valores = [] #array de los geringosos
    
    i = 0
    
    vocal = ['a','e','i','o','u','A','E','I','O','U']
    
    geringosa = ''
    
    while i < len(lista): #itera entre las palabras
        for v in lista[i]:    #itera entre las letras de cada palabras
            if v in vocal:   
                geringosa = geringosa + v + "p" + v
            else: geringosa = geringosa + v
            #print(geringosa)
            
        valores.append(geringosa) #envialo al array VALORES
        geringosa = '' #vacia geringosa
        i = i + 1    #avanza en la posición
        
    #print(valores)
    
    x = 0
    d = {}            #crea un diccionario
    
    while x < len(lista):           #itera entre cualquiera de las 2 listas
        d[lista[x]] = valores[x]    #agrega las llaves y valores
        x = x + 1                   #avanza en la iteración
    #print(d)
    return d

lista = ['banana', 'manzana', 'mandarina']
print(gering(lista))