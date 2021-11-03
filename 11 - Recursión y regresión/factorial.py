# -*- coding: utf-8 -*-
"""
Created on Tue Oct 26 21:17:55 2021

@author: Manjuanel
"""

#FACTORIAL

# def factorial(n):
#     if n == 1:
#         return 1
#     return n * factorial(n-1)

#Otro factorial detallado:
def factorial(n):
    if n == 1:
        r = 1
        return r

    f = factorial(n-1)
    r = n * f
    return r

factorial(3)
