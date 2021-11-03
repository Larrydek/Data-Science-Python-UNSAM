# -*- coding: utf-8 -*-
"""
Created on Thu Oct 14 19:53:22 2021

@author: Manjuanel
"""

class Canguro():
    def __init__(self, nombre, contenido = []):
        ''' CREA UN MARSUPIAL
            CON SU NOMBRE
            Y SU CONTENIDO [] '''
        self.nombre = nombre
        self.contenido_marsupio = contenido
        
    def meter_en_marsupio(self, x):
        ''' METE ALGO (x) EN LA BOLSA DEL MARSUPIAL '''
        self.contenido_marsupio.append(x)
        
    def __str__(self):
        ''' DEVUELVE UNA REPRESENTACIÓN DEL CANGURO
        EN TIPO CADENA'''