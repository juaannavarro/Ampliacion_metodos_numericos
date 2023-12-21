import numpy as np
import matplotlib.pyplot as plt

def euler_method(a, b, f, x0, y0, y1, h, x_final):
    """
    Resuelve la ecuación diferencial y'' + a(x)y' + b(x)y = f(x) usando el método de Euler.
    
    Parámetros:
    a, b, f: Funciones de Python que representan a(x), b(x) y f(x).
    x0, y0, y1: Condiciones iniciales x0, y(x0) y y'(x0).
    h: Tamaño del paso.
    x_final: Valor final de x para el que resolver la ecuación.
    
    Retorna:
    x_values, y_values: Arrays de los valores de x y y.
    """
    # Inicializar listas para almacenar los resultados
    x_values = [x0]
    u_values = [y0]
    v_values = [y1]

    # Bucle para aplicar el Método de Euler
    while x_values[-1] + h <= x_final:
        x_k = x_values[-1]
        u_k = u_values[-1]
        v_k = v_values[-1]

        # Aplicar las fórmulas del Método de Euler
        x_k1 = x_k + h
        u_k1 = u_k + h * v_k
        v_k1 = v_k + h * (-b(x_k) * u_k - a(x_k) * v_k + f(x_k))

        # Añadir los nuevos valores a las listas
        x_values.append(x_k1)
        u_values.append(u_k1)
        v_values.append(v_k1)

    return x_values, u_values
a = lambda x: -(2*x)/1-x**2
b = lambda x: (n*(n+1))/(1-x**2)
f = lambda x:0
n = 0
x0, y0, y1, h, x_final = 0, 1, 0, 0.00001, 0.95
x_values, y_values = euler_method(a, b, f, x0, y0, y1, h, x_final)

plt.plot(x_values, y_values)
plt.xlabel('x')
plt.ylabel('y')
plt.title('Solución por el Método de Euler')
plt.show()
