##Dérivée de la variable de la température

def delta_temperature_capteur1():
    """Cette fonction est la même pour les capteurs 2,3,4,5 et 6 en changeant la variable A. Pour le capteur 2, A=sep_capteur2()[0] et etc pour les capteurs 3,4,5,6"""
    A=sep_capteur1()[0]
    L=[0]
    for i in range(1,len(A)):
        j=(A[i]-A[i-1])
        L.append(j)
    return L

##Dérivée de la variable du bruit

def delta_bruit_capteur1():
"""Cette fonction est la même pour les capteurs 2,3,4,5 et 6 en changeant la variable A. Pour le capteur 2, A=sep_capteur2()[2] et etc pour les capteurs 3,4,5,6"""
    A=sep_capteur1()[2]
    L=[0]
    for i in range(1,len(A)):
        j=(A[i]-A[i-1])
        L.append(j)
    return L

##Dérivée de la variable de l'humidité
def delta_humidité_capteur1():
  """Cette fonction est la même pour les capteurs 2,3,4,5 et 6 en changeant la variable A. Pour le capteur 2, A=sep_capteur2()[3] et etc pour les capteurs 3,4,5,6"""
    A=sep_capteur1()[3]
    L=[0]
    for i in range(1,len(A)):
        j=(A[i]-A[i-1])
        L.append(j)
    return L

##Dérivée de la variable de la luminosité
def delta_luminosité_capteur1():
  """Cette fonction est la même pour les capteurs 2,3,4,5 et 6 en changeant la variable A. Pour le capteur 2, A=sep_capteur2()[4] et etc pour les capteurs 3,4,5,6"""
    A=sep_capteur1()[4]
    L=[0]
    for i in range(1,len(A)):
        j=(A[i]-A[i-1])
        L.append(j)
    return L

##Dérivée de la variable du CO2

def delta_CO2_capteur1():
    """Cette fonction est la même pour les capteurs 2,3,4,5 et 6 en changeant la variable A. Pour le capteur 2, A=sep_capteur2()[5] et etc pour les capteurs 3,4,5,6"""
    A=sep_capteur1()[5]
    L=[0]
    for i in range(1,len(A)):
        j=(A[i]-A[i-1])
        L.append(j)
    return L


