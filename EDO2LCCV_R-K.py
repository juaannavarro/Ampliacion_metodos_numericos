import numpy as np
import matplotlib.pyplot as plt

def runge_kutta_4th_order(a, b, f, x0, y0, y1, h, x_final):
    # Inicializar listas para almacenar los resultados
    x_values = [x0]
    u_values = [y0]
    v_values = [y1]

    # Funciones para el sistema de EDOs
    def du_dx(x, u, v):
        return v

    def dv_dx(x, u, v):
        return -a(x) * v - b(x) * u + f(x)

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


a = lambda x: 1
b = lambda x: 1
f = lambda x: 1
x0, y0, y1, h, x_final = 0, 0, 1, 0.0001, 8
x_values, y_values = runge_kutta_4th_order(a, b, f, x0, y0, y1, h, x_final)

plt.plot(x_values, y_values)
plt.xlabel('x')
plt.ylabel('y')
plt.title('Solución de la EDO por Runge-Kutta de orden 4')
plt.grid(True)
plt.show()
