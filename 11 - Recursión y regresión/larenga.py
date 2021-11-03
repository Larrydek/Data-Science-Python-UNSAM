# -*- coding: utf-8 -*-
"""
Created on Wed Oct 27 12:48:09 2021

@author: Manjuanel
"""

def pascal(n,k):
    if n == 0 or k == 0 or k == n:
        return 1    #Casos base: Los extremos del triángulo valen 1
    valor = pascal(n - 1, k - 1) + pascal(n - 1 , k) #Va volviendo hacia arriba en el triangulo para sumar los dos anteriores.
                                                        #Cuando llega, cumple los casos base
    return valor

print(pascal(10,5))
    
print(pascal(43,7))
