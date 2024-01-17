import matplotlib.pyplot as plt
import numpy as np

# Parámetros
M = 10
m = 0
k = 0.5
g = 9.8

# Ecuación diferencial
def f(t, v):
    return g - ((k - m)/(M - (m*t))) * v

# Método de Euler
def euler(f, t0, v0, h, n):
    t_values = [t0]
    v_values = [v0]
    t = t0
    v = v0
    for _ in range(1, n):
        v = v + h * f(t, v)
        t = t + h
        t_values.append(t)
        v_values.append(v)
    return t_values, v_values

# Configuración inicial
t_inicial = 0
t_final = 100
n = 2000
h = (t_final - t_inicial) / n

# Calculando la solución numérica
t_values, v_values = euler(f, t_inicial, 0, h, n)

# Gráfico
plt.plot(t_values, v_values, label='Euler')
plt.xlabel('Tiempo (t)')
plt.ylabel('Velocidad (v)')
plt.title('Solución numérica de la EDO')
plt.legend()
plt.show()
