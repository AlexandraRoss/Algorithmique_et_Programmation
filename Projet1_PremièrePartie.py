import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

df =pd.read_csv((r'/Users/alexandraross/Documents/eivp/informatique/post-32566-EIVP_KM.csv'),sep=';')
print(df)

##Évolution d'une variable en fonction du temps

def sep_capteur1():
    """Cette fonction est la même pour les capteurs 2,3,4,5 et 6 en changeant la ligne "if df.id[i]==2 ou 3,4,5,6.
    Ils ne sont pas cependant pas ceux que nous avons utilisés, nous avons créé une fonction sep() bien plus facile à utiliser"""
    A,B,C,D,E,F=[],[],[],[],[],[]
    for i in range (len(df)):
        if df.id[i]==1:
            A.append(df.temp[i])
            B.append(df.sent_at[i])
            C.append(df.noise[i])
            D.append(df.humidity[i])
            E.append(df.lum[i])
            F.append(df.co2[i])
    return A,B,C,D,E,F
a=np.array(sep_capteur1()[0])
b=np.array(sep_capteur1()[1])
c=np.array(sep_capteur1()[2])
d=np.array(sep_capteur1()[3])
e=np.array(sep_capteur1()[4])
f=np.array(sep_capteur1()[5])

plt.plot(b,a)
plt.plot(b,c)
plt.plot(b,d)
plt.plot(b,e)
plt.plot(b,f)

plt.show()

def sep(k):
	A,B,C,D,E,F=[],[],[],[],[],[]
	for i in range (len(df)):
		if df.id[i]==k:
			A.append(df.temp[i])
			B.append(df.sent_at[i])
			C.append(df.noise[i])
			D.append(df.humidity[i])
			E.append(df.lum[i])
			F.append(df.co2[i])
	return A,B,C,D,E,F

k=int(input('Quel capteur:'))
a=np.array(sep(k)[0])
b=np.array(sep(k)[1])
c=np.array(sep(k)[2])
d=np.array(sep(k)[3])
e=np.array(sep(k)[4])
f=np.array(sep(k)[5])

plt.plot(b,a,label='temperature')
plt.plot(b,c,label='bruit')
plt.plot(b,d,label='humidité')
plt.plot(b,e,label='luminosité')
plt.plot(b,f,label='CO2')
plt.legend()
plt.title('Evolution temporelle des variables du capteur choisi')

plt.show()




def inter(deb,fin):
    T,X=[],[]
    A=sep()[0]
    B=sep()[1]
    for i in range (len(B)):
        if deb<=B[i]<=fin:
            T.append(B[i])
            X.append(A[i])
    return T,X

b=np.array(inter('2019-08-11 11:17:21 +02:00','2019-08-13 01:17:21 +02:00')[0])
a=np.array(inter('2019-08-11 11:17:21 +02:00','2019-08-13 01:17:21 +02:00')[1])
plt.plot(b,a)

plt.show()

def sep_reduite():
"""Expliquée dans la partie 2 du projet et utilisée dans la SecondePartie_VersionFinale"""
    A,B=[],[]
    for i in range (len(df)):
        if df.id[i]==k:
            A.append(legende()[i])
            B.append(df.sent_at[i])
    return A,B


##Afficher les valeurs
def max():
	L=sep_reduite()[0]
	T=sep_redute()[1]
	max=L[0]
	k=0
	for i in range(1,len(L)):
		if L[i]>max:
			max=L[i]
			k=i
	return max,T[k]

def min():
	L=sep_reduite()[0]
	T=sep_reduite()[1]
	min=L[0]
	k=0
	for i in range(1,len(L)):
		if L[i]<min:
			min=L[i]
			k=i
	return min,T[k]

def moyenne():
	l=sep_reduite()[0]
	moyen=0
	n=len(l)
	for x in l:
		moyen=moyen+x
		moyen=moyen/n
	return moyen

def mediane(l):
    l=quickSort(l)
    mediane=0
    n=len(l)
    if n%2==0:
        a=l[n//2]
        b=l[(n//2)+1]
        mediane=moyenne((a,b))
    else:
        mediane=l[n//2]
    return mediane

def variance(l):
    m=moyenne(l)
    v=0
    for k in range(len(l)):
        v=v+(l[k]-m)**2
    return(v/len(l))

def ecart_type(l):
    var=variance(l)
    return var**(1/2)

def courbe():
	m=moyenne()
	X=[]
	L=sep_reduite()[0]
	for i in range(len(L)):
		X.append(m)
	return X

a=np.array(sep11()[0])
b=np.array(sep11()[1])
plt.plot(b,a)

c=np.array(courbe())
x=min()[0]
y=min()[1]
q=max()[0]
r=max()[1]
plt.plot(y,x,marker="o", color="red",label='minimum')
plt.plot(r,q,marker="o", color="green",label='maximum')
plt.plot(b,c,label='moyenne')
plt.legend()
plt.show() 


def partition(arr, bas, haut):
    i = (bas-1)
    pivot = arr[haut]
    for j in range(bas, haut):
        if arr[j] <= pivot:
            i = i+1
            arr[i], arr[j] = arr[j], arr[i]
    arr[i+1], arr[haut] = arr[haut], arr[i+1]
    return (i+1)

def quickSort(arr, bas, haut):
    if len(arr) == 1:
        return arr
    if bas < haut:
        pi = partition(arr, bas, haut)
        quickSort(arr, bas, pi-1)
        quickSort(arr, pi+1, haut)

##Calcul de l'indice humidex
def rose():
    a=17.27
    b=237.7
    Tr=[]
    T=sep()[0]
    H=sep()[2]
    n=len(T)
    for i in range(n):
        c=T[i]
        d=H[i]/100
        alpha=(a*c/(b+c))+math.log(d)
        t=(b*alpha)/(a-alpha)
        Tr.append(t)
    return Tr

def humidex():
    Tr=rose()
    T=sep()[0]
    Hum=[]
    n=len(T)
    for i in range(n):
        h=T[i]+0.5555*(6.11*math.exp(5417.753*(1/273.16-1/(273.15+Tr[i])))-10)
        Hum.append(h)
    return Hum

##Calcul de l'indice de corrélation entre un couple de variables
def cov(X,Y):
    n=len(X)
    T=0
    J=0
    for i in range (n):
        T+=(((X[i]-moyenne(X))*(Y[i]-moyenne(Y))))
        J=(T/(n))
    return J

def cor(X,Y):
    p=cov(X,Y)/((variance(X)*variance(Y))**(1/2))
    return p

##Fonctions supplémentaires

def separation(d):
    return ([int(d[0:4]),int(d[5:7]),int(d[8:10])])

def date(d):
    heure=int(d[11:13])
    minute=int(d[14:16])
    seconde=int(d[17:19])
    return (heure*3600+minute*60+seconde)

def distance(d):
    init=min(sep()[1])
    jour_init=separation(init)[2]
    jour=separation(d)[2]
    mois_init=separation(init)[1]
    mois=separation(d)[1]
    if jour>jour_init:
        return ((jour-jour_init-1)*86400+date(d)+86400-date(init))
    else:
        return (date(d)-date(init))

def liste():
    A=sep()[1]
    L=[]
    for i in range(len(A)):
        L.append(distance(A[i]))
    return L
