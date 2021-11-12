# -*- coding: utf-8 -*-
"""
Created on Tue Nov  9 19:19:18 2021

@author: Manjuanel
"""
#Imports
import seaborn as sns
import pandas as pd
from sklearn.datasets import load_iris

iris_dataset = load_iris()
iris_dataframe = pd.DataFrame(iris_dataset['data'], columns = iris_dataset.feature_names)

print(iris_dataframe)
# sns.pairplot(data = iris_dataframe,kind='scatter')
iris_dataframe['Species'] = iris_dataset['target']

print(iris_dataframe)
sns.pairplot(iris_dataframe, hue='Species')

