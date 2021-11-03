# -*- coding: utf-8 -*-
"""
Created on Wed Oct 13 12:32:41 2021

@author: Manjuanel
"""
#%%
#EJERCICIO 9.12: TORRE DE CONTROL
class Cola:
    '''Representa a una cola, con operaciones de encolar y desencolar.
    El primero en ser encolado es tambien el primero en ser desencolado.
    '''

    def __init__(self):
        '''Crea una cola vacia.'''
        self.items = []

    def encolar(self, x):
        '''Encola el elemento x.'''
        self.items.append(x)

    def desencolar(self):
        '''Elimina el primer elemento de la cola 
        y devuelve su valor. 
        Si la cola esta vacia, levanta ValueError.'''
        if self.esta_vacia():
            raise ValueError('La cola esta vacia')
        return self.items.pop(0)

    def esta_vacia(self):
        '''Devuelve 
        True si la cola esta vacia, 
        False si no.'''
        return len(self.items) == 0
    
    def join(self, c =''):
        if self.esta_vacia():
            return ''
        return c.join(self.items)

class TorreDeControl(Cola):
    '''Representa a una torre de control que contiene dos colas'''

    def __init__(self):
        '''Crea una torre vacia.'''
        self.arribos = Cola()
        self.partidas = Cola()

    def nuevo_arribo(self, a):
        '''Encola el arribo'''
        self.arribos.encolar(a)

    def nueva_partida(self, p):
        '''Encola la partida'''
        self.partidas.encolar(p)

    def asignar_pista(self):
        '''Asigna una pista a los vuelos que aterrizan, y si no hay a los que despegan 
        Si la torre esta vacia, levanta ValueError.'''
        if(self.arribos.esta_vacia()):
            if(self.partidas.esta_vacia()):
                print("No hay vuelos en espera")
            else:
                print(f'El vuelo {self.partidas.desencolar} despegó con éxito')
        print(f'El vuelo {self.arribos.desencolar} aterrizó con éxito')
    
    def ver_estado(self):
        arribos = self.arribos.join(', ')
        partidas = self.partidas.join(', ')
        print(f'Vuelos esperando para aterrizar: {arribos}')
        print(f'Vuelos esperando para despegar: {partidas}')
        
torre = TorreDeControl()
torre.nuevo_arribo('ar12')
torre.nueva_partida('klm12')
torre.nuevo_arribo('ar420')
torre.ver_estado()
