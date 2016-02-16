
# coding: utf-8

# In[4]:

#importo la funcion sqrt de math
from math import sqrt

#pido altura al usuario
h = float(input("Proporciona la altura en metros de la torre: "))
g=9.81
t=sqrt(2*h/g) #Calculo de tiempo de caida

#Impresion de Resultados
print ("El tiempo de caida es:", t ,"s")


# In[7]:

from math import pi
G=6.67e-11
m=5.97e24
r=6371000
t= float(input("ingresa el periodo del satélite:"))
T= t*60
a=(g*m*t*t) / (4*pi*pi)
b=a**(1./3.)
Y=b-r
print ("La altura del satélite es", h, "metros.")


# In[8]:

from math import pi, sin, atan, acos, sqrt
print ("Especifica las coordenadas cartesianas del punto:")
x = float(input("Introduce x: "))
y = float(input("Introduce y: "))
z = float(input("Inytoduce z: "))
r = sqrt(x**2 + y**2 + z**2)
theta = acos(z/r)
phi = atan(y/x)
print ("Las coordenas esféricas son:")
print("r =",r,"theta =",theta,"phi =",phi)


# In[9]:

n,C1,C2 = 0,1,1
while(C2 < 1000000): 
    print(C2)
    C2= C1*(4*n+2)/(n+2)
    n=n+1
    C1=C2


# In[ ]:



