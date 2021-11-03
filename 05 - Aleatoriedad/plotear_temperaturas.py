# -*- coding: utf-8 -*-
"""
Created on Tue Sep  7 22:26:39 2021

@author: Manjuanel
"""

import numpy as np
import matplotlib.pyplot as plt

def plotear_temperaturas():
        temperaturas = np.load('../Data/temperaturas.npy')
        plt.hist(temperaturas[0,:],bins=10) #El [0,:] es porque el array es 1x999, es decir, 1 fila, 999 columnas. [0] (Primer fila) [:] (Columnas restantes)
        plt.show()
        return
        
        
print(plotear_temperaturas())