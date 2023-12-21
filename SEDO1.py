import numpy as np
import matplotlib.pyplot as plt
#x=u, y=v
def runge_kutta_predator_prey(p, q, r, s, x0, y0, h, t_final):
    t_values = [0]
    x_values = [x0]
    y_values = [y0]

    while t_values[-1] + h <= t_final:
        t = t_values[-1]
        x = x_values[-1]
        y = y_values[-1]

        fx = lambda x, y: -y + x *(1-x * x -y* y)
        fy = lambda x, y: x + y *(1-x * x -y* y)

        k1x = h * fx(x, y)
        k1y = h * fy(x, y)
        k2x = h * fx(x + 0.5 * k1x, y + 0.5 * k1y)
        k2y = h * fy(x + 0.5 * k1x, y + 0.5 * k1y)
        k3x = h * fx(x + 0.5 * k2x, y + 0.5 * k2y)
        k3y = h * fy(x + 0.5 * k2x, y + 0.5 * k2y)
        k4x = h * fx(x + k3x, y + k3y)
        k4y = h * fy(x + k3x, y + k3y)

        x_next = x + (k1x + 2 * k2x + 2 * k3x + k4x) / 6
        y_next = y + (k1y + 2 * k2y + 2 * k3y + k4y) / 6

        t_values.append(t + h)
        x_values.append(x_next)
        y_values.append(y_next)

    return t_values, x_values, y_values

# Parámetros y condiciones iniciales
p, q, r, s = 3, 1, 2, 1
x0, y0 = 0,5
h = 0.1
t_final = 20


# Resolver el sistema
t_values, x_values, y_values = runge_kutta_predator_prey(p, q, r, s, x0, y0, h, t_final)

# Graficar los resultados
plt.figure(figsize=(12, 6))
plt.subplot(1, 2, 1)
plt.plot(t_values, x_values, label='Presa (x)')
plt.plot(t_values, y_values, label='Depredador (y)')
plt.xlabel('Tiempo (t)')
plt.ylabel('Poblaciones')
plt.title('Dinámica de Poblaciones Depredador-Presa')
plt.legend()
plt.grid(True)

plt.subplot(1, 2, 2)
plt.plot(x_values, y_values)
plt.xlabel('Presa (x)')
plt.ylabel('Depredador (y)')
plt.title('Espacio de Fase')
plt.grid(True)

plt.tight_layout()
plt.show()



