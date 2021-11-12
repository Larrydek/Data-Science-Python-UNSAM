# -*- coding: utf-8 -*-
"""
Created on Tue Oct 26 12:43:19 2021

@author: Manjuanel
"""
#Imparidad recursiva

def es_impar(n):
    
    if n == 0:
        res = False
    else: 
        temp = es_impar(n-1)  
        res = not temp     #EL PROGRAMA "DA VUELTA" EL VALOR DE TEMP TANTAS VECES COMO VUELTAS DE HASTA LLEGAR A 0        
    return res



es_impar(3)

#Mucha recursión. No lo calcula