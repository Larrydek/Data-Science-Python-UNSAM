# -*- coding: utf-8 -*-
"""
Created on Wed Oct 27 00:18:42 2021

@author: Manjuanel
"""

#FIBONACCI

def fibonacci(n):
    '''
    Calcula el número [n] de la sucesión de fibonacci
    '''
    if n == 0 or n == 1:
        return n
    ant2 = 0            #primer valor
    ant1 = 1            #segundo valor
    
    for i in range(2, n + 1):
        fibn = ant2 + ant1
        ant2 = ant1  
        ant1 = fibn
    return fibn