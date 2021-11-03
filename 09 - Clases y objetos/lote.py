# -*- coding: utf-8 -*-
"""
Created on Tue Oct 12 13:37:21 2021

@author: Manjuanel
"""
#%%
#EJERCICIO 9.9: Lote.py
class Lote():
    def __init__(self, nombre, cajones, precio):
        self.nombre = nombre
        self.cajones = cajones
        self.precio = precio
    
    #PARA QUE SE VEA LINDO:
    def __repr__(self):
        return f'Lote({self.nombre},{self.cajones},{self.precio})'
    
    def __str__(self):
        return f'Lote de {self.cajones} de {self.nombre}, pagados a ${self.precio} cada uno'
     
    def costo(self):
        return self.cajones * self.precio
    
    def vender(self, cantidad):
        self.cajones -= cantidad
        

        

