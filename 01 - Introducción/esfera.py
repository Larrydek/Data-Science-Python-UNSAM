# -*- coding: utf-8 -*-
"""
Created on Mon Aug  9 18:42:10 2021

@author: Manjuanel
"""

#volumen de la esfera
import math

r = input('Ingrese radio de la esfera: ')
r = int(r)
v = 4/3 * math.pi * (r ** 3)
print(r)
print('El volumen de la esfera es: ',v)
