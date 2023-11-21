import matplotlib.pyplot as plt
import numpy as np


def runge_kutta_4(f, x, y, h, n):
    '''
    Función que implementa el método de Runge-Kutta de orden 4 para resolver una EDO
    '''
    u = []
    v = []
    for i in range(n):
        k1 = f(x, y)
        k2 = f(x + (h/2), y + ((h/2) * k1))
        k3 = f(x + (h/2), y + ((h/2) * k2))
        k4 = f(x + h, y + (h * k3))

        y = y + h * (((1/6) * k1) + ((1/3) * k2) + ((1/3) * k3) + ((1/6) * k4))
        x = x + h
        u.append(x)
        v.append(y)
    return u, v

def f(x, y):
    '''
    Aquí se define la EDO
    '''
    return y - x**2 + 1

def f_exacta(x):
    '''
    Función exacta
    '''
    return (x + 1)**2 - (1/2)*np.exp(x)

def error(v, v_aprox):
    '''
    Devuelve el error absoluto
    '''
    return abs(v - v_aprox)


# DATOS
# -----
# Rango de x
x_inicial = 0
x_final = 1/2
# Datos iniciales
x = 0
y = 1/2
# Número de subintervalos que nos permite calcular el valor de h (paso)
n = 5
h = (x_final - x_inicial)/n

# Aplicamos el método de Runge-Kutta de orden 4
u, v = runge_kutta_4(f, x, y, h, n)

# Imprimimos la última y del bucle con 7 decimales
print('w_100: {:.7f}'.format(v[-1]))

# Imprimimos la solución exacta con 7 decimales
print('y(',x_final,'): {:.7f}'.format(f_exacta(x_final)) )

# Error absoluto con 7 decimales
print('Error: {:.7f}'.format(error(f_exacta(x_final), v[-1])))

# Graficar la solución
'''plt.plot(u, v)
plt.grid(True)
plt.show()'''