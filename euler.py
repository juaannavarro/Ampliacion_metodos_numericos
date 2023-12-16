import matplotlib.pyplot as plt
import numpy as np


#EJERCIO APLICANDO EULER
def euler(f,x,y,h,m):
    u = []
    v = []
    for i in range(m):
        y = y + h*f(x,y)
        x = x + h
        u.append(x)
        v.append(y)
    return u,v

def f(x,y):
    '''Aqui añadimos la EDO'''
    return (np.exp(x))/(1+np.exp(x)*y)


x = -2#Esto se modifica
y = 1 #Esto se modifica
h = 0.04 #Esto se modifica
m = 100 #Esto se modifica
u,v = euler(f,x,y,h,m)

print('w_100', v[-1])

def error(v,v_aprox):
    return abs(v-v_aprox)

print('Error: ', error(2.2202,v[-1]))

#Grafica
plt.plot(u,v,label='Euler')
plt.xlabel('x')
plt.ylabel('y')
plt.legend()
plt.show()

