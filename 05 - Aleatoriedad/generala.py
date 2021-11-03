# -*- coding: utf-8 -*-
"""
Created on Mon Sep  6 15:46:56 2021

@author: Manjuanel
"""

#Ejercicio 5.1: GENERALA
import random

#TIRA DADOS:
def tirar():
    tirada = []
    
    for i in range(5):          #crea la lista de números
        tirada.append(random.randint(1,6))
    
    def repetidor(): #ELIGE EL NUMERO REPETIDO
        repetido = 0
        counter = 0
        for x in tirada:        #selecciona el número que más se repite
            if tirada.count(x) >= counter:
                counter = tirada.count(x)
                repetido = x    #elegí el que más se repite
            else: 
                pass
        return repetido
    repetido = repetidor()
    print(f'primer tirada: {tirada}')
    print(f'numero repetido: {repetido}')
    
    n = 0        
    while n < 3:    # 3 TIRADAS
        repetidor()                 #checkea cual se repite más ahora
        repetido = repetidor() 
        print(f'nuevo repetido: {repetido}')
        z = 0
        while z < len(tirada) - 1:
            if tirada[z] != repetido:           #si es distinto del repetido
                tirada[z] = random.randint(1,6) #volve a tirar
            z = z + 1
        n += 1
        print(f'{n} nueva tirada {tirada}')
        
        
    return tirada


    
#CHECKEA SI ES GENERALA:
def es_generala(tirada):
    check = True
    
    for x in tirada:
        if x != tirada[0]:
            check = False
    return check

tirada = tirar()
print(es_generala(tirada))

#CÁLCULO DE PROBABILIDAD
def prob_generala(N):
    G = sum([es_generala(tirar()) for i in range(N)])
    prob = G/N
    print(f'Tiré {N} veces, de las cuales {G} saqué generala.')
    print(f'Podemos estimar la probabilidad de sacar generala mediante {prob:.6f}.')
    return prob

N = 10000

print(prob_generala(N))



