# -*- coding: utf-8 -*-
"""
Created on Wed Oct  6 00:23:29 2021

@author: Manjuanel
"""

#Pandas
#IMPORTS:
import pandas as pd
import os
import seaborn as sns
import matplotlib.pyplot as plt

##SOBRE LOS NOMBRES ESCRITOS DIFERENTES:
## CONTAR EN CUALES SON MENOS Y ELEGIR ESE (MENOS COMPUTO)
## REEMPLAZARLOS POR LOS NOMBRES DEL OTRO

directorio = '../Data'
archivo_parques = 'arbolado-en-espacios-verdes.csv'
archivo_vereda = 'arbolado-publico-lineal-2017-2018.csv'

def armar_dataframe(directorio, archivo): #ARMA DATAFRAME
    path = os.path.join(directorio, archivo)
    df = pd.read_csv(path)
    return df


def armar_columnas(df, cols, nombre):
    cols_selec = cols
    df_cols = df[cols_selec]
    df_cols = df_cols.rename(columns = {cols[0]: "nombre", cols[1]: "diametro", cols[2]: "altura"})
    df_cols = df_cols[df_cols['nombre'] == nombre]
    return df_cols

    
cols_parque = ['nombre_cie', 'diametro', 'altura_tot'] #COLUMNAS A SELECCIONAR
cols_vereda = ['nombre_cientifico', 'diametro_altura_pecho', 'altura_arbol']

df_parques = armar_dataframe(directorio, archivo_parques).copy()
#print(df_parques)
df_vereda = armar_dataframe(directorio, archivo_vereda).copy()
#print(df_vereda)


df_tipas_parques = armar_columnas(df_parques, cols_parque, 'Tipuana Tipu')
df_tipas_parques = df_tipas_parques.assign(ambiente = 'parque')
df_tipas_veredas = armar_columnas(df_vereda, cols_vereda, 'Tipuana tipu')
df_tipas_veredas = df_tipas_veredas.assign(ambiente = 'vereda')


df_tipas = pd.concat([df_tipas_veredas, df_tipas_parques])

print(df_tipas)


#ASÍ SE BOXPLOTEA SOLO CON PYTHON
#df_tipas.boxplot('diametro',by = 'ambiente') 
#df_tipas.boxplot('altura',by = 'ambiente')


plt.figure()
fig1 = sns.boxplot(data = df_tipas, x = 'ambiente', y = 'diametro')
plt.show()

plt.figure()
fig2 = sns.boxplot(data = df_tipas, x = 'ambiente', y = 'altura')
plt.show()






