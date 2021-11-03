# -*- coding: utf-8 -*-
"""
Created on Tue Oct 19 12:33:19 2021

@author: Manjuanel
"""

# camion.py

class Camion:

    def __init__(self, lotes):
        self.lotes = lotes
        
    def __iter__(self):                 #HACE ITERABLE EL OBJETO CAMION
        return self.lotes.__iter__()
    
    def __contains__(self, nombre):
        return any(lote.nombre == nombre for lote in self.lotes) #Hecha con generador
    
    def __len__(self):
        return self.lotes.__len__()
    
    def __getitem__(self, nombre):
        return self.lotes.__getitem__(nombre)

    def precio_total(self):
        return sum(l.costo() for l in self.lotes) #Hecha con generador

    def contar_cajones(self):
        from collections import Counter
        cantidad_total = Counter()
        for l in self.lotes:
            cantidad_total[l.nombre] += l.cajones
        return cantidad_total
    
    def __repr__(self):    
        return f'Camion({self[0:len(self)]})'
    
    def __str__(self):
        t = [f'Camion con {len(self)} lotes:']
        for i in self.lotes:
            t.append(i.__str__())
            
        return '\n'.join(t)

    
if __name__ == '__main__':
    import informe_final
    camion = informe_final.leer_camion('../Data/camion.csv')
    print(camion.precio_total())

