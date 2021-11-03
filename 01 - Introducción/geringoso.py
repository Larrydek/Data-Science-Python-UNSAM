# -*- coding: utf-8 -*-
"""
Created on Mon Aug  9 19:07:24 2021

@author: Manjuanel
"""

#Geringoso



cadena = input('Escribi y te lo mando al geringoso: ')

vocal = ['a','e','i','o','u','A','E','I','O','U']

geringosa = ''

for v in cadena:
    if v in vocal:
        geringosa = geringosa + v + "p" + v
    else: geringosa = geringosa + v

print(geringosa)
        