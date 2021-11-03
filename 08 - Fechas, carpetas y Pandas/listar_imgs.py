# -*- coding: utf-8 -*-
"""
Created on Mon Oct  4 14:43:58 2021

@author: Manjuanel
"""
#Imports
import os

#Función
def archivos_png(directorio):
    '''
    TOMA UN PATH 
    Y MUESTRA UNA LISTA
    DE TODO LO DE ADENTRO
    '''
    
    lista_archivos = os.listdir(directorio)
    print(lista_archivos)
    return lista_archivos


#Bloque MAIN:
  
if __name__ == '__main__':
    import sys
    if len(sys.argv) == 2:
        archivos_png(sys.argv[1]) #PASALE EL 2DO ARGUMENTO (RUTA) EN LA FUNCIÓN
        
        





    