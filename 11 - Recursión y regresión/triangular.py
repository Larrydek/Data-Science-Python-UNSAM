# -*- coding: utf-8 -*-
"""
Created on Wed Oct 27 09:50:11 2021

@author: Manjuanel
"""

#Ejercicio 11.2: Números triangulares

def triangular(n):
    '''
    Calcula el número triangular
    '''
    if n == 1:          #Caso base
        res = 1
        return res
    
    t = triangular(n-1) #Caso recursivo
    res = n + t
    return res

#Pruebas:
# triangular(4)
# triangular(10)
triangular(10000)
# 10 + 9 + 8 + 7 + 6 + 5 + 4 + + 3 + 2 + 1 
