import matplotlib.pyplot as plt
import numpy as np


#EJERCIO APLICANDO EULER
def euler(f,x,y,h,n):
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
    #return (np.exp(x))/((1+np.exp(x))*y)
    return (1+4*x*y)/(3*x**2)

def f_exacta(x):
    '''Aqui añadimos la solucion exacta'''
    #return np.sqrt(2 * np.log(1 + np.exp(x)) + 0.746144)
    return (-1)/(7*x) -1.8*x**(4/3)




def error(v, v_aprox):
    '''
    Devuelve el error absoluto
    '''
    return abs(v - v_aprox)

#DATOS
x_inicial=0.5
x_final=4

x = 0.5
y = -1 
n = 100 
h = (x_final-x_inicial)/n
u,v = euler(f,x,y,h,n)

print('w_100', v[-1])

#solucion real en y(2)
print('y(4)=', f_exacta(4)) #es la ultima x del rango

#Error
v_exacta = f_exacta(4)
print('Error: ', error(v_exacta,v[-1]))

#Grafica
plt.plot(u,v,label='Euler')
plt.xlabel('x')
plt.ylabel('y')
plt.legend()
plt.show()

