# -*- coding: utf-8 -*-
"""
Created on Wed Aug 25 11:12:46 2021

@author: Manjuanel
"""

header = [0 , 1 , 2 , 3 , 4 , 5 , 6 , 7 , 8 , 9]
 
print(f'   {header[0]:>2d}  {header[1]:>2d}  {header[2]:>2d}  {header[3]:>2d}  {header[4]:>2d}  {header[5]:>2d}  {header[6]:>2d}  {header[7]:>2d}  {header[8]:>2d}  {header[9]:>2d}')
print('---------------------------------------------')


for x in range(10):
    a = x * 0
    b = x * 1
    c = x * 2
    d = x * 3
    e = x * 4
    f = x * 5
    g = x * 6
    h = x * 7
    i = x * 8
    j = x * 9

    
    print( f'{x}: {a:>2d}  {b:>2d}  {c:>2d}  {d:>2d}  {e:>2d}  {f:>2d}  {g:>2d}  {h:>2d}  {i:>2d}  {j:>2d}' ) 