# -*- coding: utf-8 -*-
"""
Created on Sun Jan  2 20:30:27 2022

@author: happy
"""
import pandas as pd

path=r"C:\Users\happy\Downloads\ottTheatreData.xlsx"
data=pd.read_excel(path)
print(data)
data.AA.mean()
data.OTT.mean()
data.THEATRE.mean()
data.OTT.hist()
