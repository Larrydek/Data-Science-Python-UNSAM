# -*- coding: utf-8 -*-
"""
Created on Tue Oct 12 10:22:05 2021

@author: Manjuanel
"""
#IMPORT
import pandas as pd

#READER
df = pd.read_csv('../Data/OBS_SHN_SF-BA.csv', index_col = ['Time'], parse_dates = True)

#Primeros 5 datos
df.head()

#Indices
df.index

#[DESDE, HASTA]
df['1-18-2014 9:00':'1-18-2014 18:00']
df['2-19-2014']

#plots
df['12-25-2014':].plot()
df['10-15-2014':'12-15-2014'].plot()