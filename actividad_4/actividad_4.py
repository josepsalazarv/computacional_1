
# coding: utf-8

# In[8]:

import matplotlib.pyplot as plt 
import numpy as np

datos = np.loadtxt("lineal.txt")
x=datos[:,0]
y=datos[:,1]
print (x)
print (y)

plt.plot(x,y, 'bo')
plt.show()


# In[11]:

import numpy as np
import matplotlib.pyplot as plt
from scipy import optimize

#Leyendo el archivo con los datos
datos = np.loadtxt('lineal.txt')
x=datos[:,0]
y=datos[:,1]

print (x)
print (y)

#Escribiendo con la forma de y=mx+b
fitfunc = lambda p, x: p[0]*x + p[1]

#Distancia del punto al ajuste lineal
errfunc = lambda p, x, y: fitfunc(p, x) - y 

#Parametros patito
p0 = [1, 1] 

#Optimizando la recta
p1, success = optimize.leastsq(errfunc, p0[:], args=(x, y))

#Para la grafica
time = np.linspace(x.min(), x.max(), 100)
plt.plot(x, y, "mo", label="Data") 
plt.plot(time, fitfunc(p1, time), "g-", label="Fitted curve")

plt.title("Winter temperature in New York from 1900-1999")
plt.grid()
plt.legend()
plt.xlabel("Year")
plt.ylabel("Temperature")


# In[12]:

import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit

#Leyendo el archivo con los datos
datos = np.loadtxt("exponencial.txt")
x=datos[:,0]
y=datos[:,1]
print (x)
print (y)

#Escribiendo con la forma de y=a*e^(-bx)+c
def func(x, a, b, c):
    return a * np.exp(-b * x) + c

#Generando estimacion base
yn = y + 0.2*np.random.normal(size=len(x))

#Optimizando la curva
popt, pcov = curve_fit(func, x, yn)

#Para la grafica
plt.figure()
plt.plot(x, yn, 'mo', label="Data")
plt.plot(x, func(x, *popt), 'g-', label="Fitted curve")

plt.grid()
plt.legend()
plt.title("Atmospheric pressure vs. altitude")
plt.xlabel("Altitude")
plt.ylabel("Pressure")

plt.show()

