# -*- coding: utf-8 -*-
"""
Created on Wed Sep 22 01:02:58 2021

@author: Manjuanel
"""
#%%
def valor_absoluto(n):
    '''
    PRE: EL PARÁMETRO DEBE SER UN NÚMERO
    POS: DEVUELVE EL NÚMERO POSITIVO
    
    RECIBE UN NÚMERO Y LE APLICA EL VALOR ABSOLUTO

    '''
    if n >= 0:
        return n
    else:
        return -n

#%%
def suma_pares(l):
    '''
    PRE: INGRESA UNA LISTA DE NÚMEROS (INT O FLOAT)
    POS: DEVUELVE UN NÚMERO QUE ES LA SUMA DE LOS PARES

    '''
    res = 0     #INVARIANTE ACUMULADORA
    for e in l:
        if e % 2 ==0: #SI ES PAR
            res += e  #SUMALO AL ACUMULADOR
        else:
            res += 0

    return res

l = [1,2,3,4.25,2]
print(suma_pares(l))

#%%
def veces(a, b):
    '''
    PRE: INGRESA 2 NÚMEROS
    POS: DEVUELVE UN NÚMERO QUE ES EL PRODUCTO DE LOS 2
    
    

    '''
    res = 0 #INVARIANTE ACUMULADORA
    nb = b  #CANTIDAD DE VECES QUE VA A SUMAR 'a' | INVARIANTE DE CICLO
    while nb != 0:
        #print(nb * a + res)
        res += a #LE SUMA a
        nb -= 1 #RESTA HASTA LLEGAR A 0
    return res

print(veces(7,4))

#%%
def collatz(n):
    '''
    PRE: INGRESA UN NÚMERO
    POS: DEVUELVE OTRO NÚMERO

    '''
    res = 1     #INVARIANTE ACUMULADORA

    while n!=1:    #INVARIANTE DE CICLO |
        if n % 2 == 0: #SI ES PAR:
            n = n//2   #DIVIDILO A LA MITAD
        else:   	   #SI ES IMPAR:
            n = 3 * n + 1
        res += 1

    return res

print('----------------------')
print(collatz(1))
print(collatz(500))
print(collatz(125))
print(collatz(100))
print(collatz(75))



