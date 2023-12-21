import numpy as np
import matplotlib.pyplot as plt
import math

def calcular_yp0(n):
    """
    Calcula y'(0) para la ecuación diferencial de Chebyshev con el valor dado de n.

    Parámetros:
    n: Valor entero que representa el parámetro n en la ecuación.

    Retorna:
    Valor de y'(0) calculado.
    """
    suma = 0
    for m in range(math.floor(n / 2) + 1):
        termino = ((-1)**m * math.factorial(n - m - 1) / (math.factorial(m) * math.factorial(n - 2 * m - 1)) * (-2)**(n - 2 * m - 1))
        suma += termino
    return n / 2 * suma
def runge_kutta_4th_order_chebyshev(n, x0, y0, yp0, h, x_final):
    """
    Resuelve la ecuación diferencial de Chebyshev (1 - x^2)y'' - xy' + n^2y = 0 usando el método de Runge-Kutta de orden 4.

    Parámetros:
    n: Parámetro n en la ecuación de Chebyshev.
    x0, y0, yp0: Condiciones iniciales.
    h: Tamaño del paso.
    x_final: Valor final de x.

    Retorna:
    x_values, y_values: Arrays de los valores de x y y.
    """
    # Inicializar listas para almacenar los resultados
    x_values = [x0]
    u_values = [y0]
    v_values = [yp0]

    # Funciones para el sistema de EDOs
    def du_dx(x, u, v):
        return v

    def dv_dx(x, u, v):
        return ((x * v - n**2 * u) / (1 - x**2)) if x != 1 and x != -1 else 0

    # Bucle para aplicar el método de Runge-Kutta de orden 4
    while x_values[-1] + h <= x_final:
        x_k = x_values[-1]
        u_k = u_values[-1]
        v_k = v_values[-1]

        # Cálculos de k para u y l para v
        k1 = h * du_dx(x_k, u_k, v_k)
        l1 = h * dv_dx(x_k, u_k, v_k)
        k2 = h * du_dx(x_k + 0.5 * h, u_k + 0.5 * k1, v_k + 0.5 * l1)
        l2 = h * dv_dx(x_k + 0.5 * h, u_k + 0.5 * k1, v_k + 0.5 * l1)
        k3 = h * du_dx(x_k + 0.5 * h, u_k + 0.5 * k2, v_k + 0.5 * l2)
        l3 = h * dv_dx(x_k + 0.5 * h, u_k + 0.5 * k2, v_k + 0.5 * l2)
        k4 = h * du_dx(x_k + h, u_k + k3, v_k + l3)
        l4 = h * dv_dx(x_k + h, u_k + k3, v_k + l3)

        # Actualización de los valores de u y v
        u_k1 = u_k + (k1 + 2 * k2 + 2 * k3 + k4) / 6
        v_k1 = v_k + (l1 + 2 * l2 + 2 * l3 + l4) / 6

        # Añadir los nuevos valores a las listas
        x_values.append(x_k + h)
        u_values.append(u_k1)
        v_values.append(v_k1)

    return x_values, u_values

# Ejemplo de uso
n = 5
x0 = -1
y0 = (-1)**n
yp0 = calcular_yp0(n)
h = 0.01
x_final = 1

x_values, y_values = runge_kutta_4th_order_chebyshev(n, x0, y0, yp0, h, x_final)

# Visualización de los resultados
plt.plot(x_values, y_values)
plt.xlabel('x')
plt.ylabel('y')
plt.title(f'Solución de la Ecuación de Chebyshev para n = {n}')
plt.grid(True)
plt.show()
