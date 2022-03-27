# -*- coding: utf-8 -*-
"""
Created on Sun Jan  2 20:30:27 2022

@author: happy
"""
import pandas as pd

path=r"C:/Users/happy/Documents/ott.xlsx"
data=pd.read_excel(path)
print(data)

data.OTT.mean()
data.THEATRE.mean()
data.OTT.mode()
data.THEATRE.mode()
data.OTT.median()
data.THEATRE.median()
data.OTT.hist()
data.OTT.describe()
data.OTT.value_counts()
data.THEATRE.describe()
data.THEATRE.value_counts()
data.OTT.unique()
data.THEATRE.unique()
