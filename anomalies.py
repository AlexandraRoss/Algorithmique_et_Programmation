# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import pandas as pd
import numpy as np


df =pd.read_csv((r'/Users/alexandraross/Desktop/post-32566-EIVP_KM.csv'),sep=';')
print(df)

def sep():
    A,B=[],[]
    for i in range (len(df)):
        if df.id[i]==6:
            A.append(df.co2[i])
            B.append(df.sent_at[i])
    return A,B

def delta():
    A=sep()[0]
    L=[0]
    for i in range(1,len(A)):
        j=(A[i]-A[i-1])
        L.append(j)
    return L

def quantile():
    L=delta()
    return np.quantile((L),[0.01,0.99])

def an():
    L=delta()
    T=sep()[1]
    H=[]
    for i in range (len(L)):
        if L[i]<quantile()[0] or L[i]>quantile()[1]:
            H.append(T[i])
    return H
