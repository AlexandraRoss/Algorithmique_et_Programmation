import pandas as pd
import numpy as np


df =pd.read_csv((r'/Users/alexandraross/Desktop/post-32566-EIVP_KM.csv'),sep=';')
print(df)



v=int(input("Choisissez un nombre selon la variable 1=temp,2=lum,3=CO2,4=humidity et 5=noise:",))

def legende():
    if v==1:
        return df.temp
    elif v==2:
        return df.lum
    elif v==3:
        return df.CO2
    elif v==4:
        return df.humidity
    else:
        return df.noise


k=int(input('Quel capteur:'))

def sep_reduite():
    A,B=[],[]
    for i in range (len(df)):
        if df.id[i]==k:
            A.append(legende()[i])
            B.append(df.sent_at[i])
    return A,B


def delta():
    A=sep_reduite()[0]
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
    T=sep_reduite()[1]
    H=[]
    for i in range (len(L)):
        if L[i]<quantile()[0] or L[i]>quantile()[1]:
            H.append(T[i])
    return H








