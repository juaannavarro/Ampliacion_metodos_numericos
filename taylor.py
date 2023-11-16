# MÉTODO DE TAYLOR -- ORDEN 2

import matplotlib.pyplot as plt


def taylor(f, df_dx, df_dy, x, y, h, n):
    '''
    Función que implementa el método de Taylor para resolver una EDO
    '''
    u = []
    v = []
    for i in range(n):
        y = y + h * f(x, y) + (h**2/2) * (df_dx(x, y) + df_dy(x, y) * f(x, y))
        x = x + h
        u.append(x)
        v.append(y)
    return u, v

def f(x, y):
    '''
    Aquí se define la EDO
    '''
    return (1 + 4*x*y)/(3*x**2)

def df_dx(x, y):
    '''
    Aquí se define la derivada parcial de f con respecto a x
    '''
    return -(4*x*y + 2)/(3*x**3)

def df_dy(x, y):
    '''
    Aquí se define la derivada parcial de f con respecto a y
    '''
    return (4)/(3*x)

def error(v, v_aprox):
    '''
    Devuelve el error absoluto
    '''
    return abs(v - v_aprox)


# DATOS
x = 0.5
y = -1
h = 0.035
n = 100

# Aplicamos el método de Euler
u, v = taylor(f, df_dx, df_dy, x, y, h, n)

# Imprimimos la última y del bucle
print('w_100: ', v[-1])

# Error
v_e = -11.46
print('Error: ', error(v_e, v[-1]))

# Graficar la solución
plt.plot(u, v)
plt.grid(True)
plt.show()
