# Definir la función
import numpy as np
import matplotlib.pyplot as plt

def f(x, y):
    return (1 + 4*x*y)/(3*x**2)

# Método de Runge-Kutta de segundo orden (Euler mejorado)
def runge_kutta_second_order(x0, y0, xn, n):
    h = (xn-x0)/float(n)
    x = np.linspace(x0, xn, n+1)
    y = np.zeros(n+1)
    y[0] = y0
    for i in range(n):
        k1 = h * f(x[i], y[i])
        k2 = h * f(x[i] + h, y[i] + k1)
        y[i+1] = y[i] + 0.5 * (k1 + k2)
    return x, y

# Parámetros
x0 = 0.5
y0 = -1
xn = 4
n = 100

# Calcular y trazar la solución con Runge-Kutta de segundo orden
x, y = runge_kutta_second_order(x0, y0, xn, n)
plt.plot(x, y, 'o-', label='Runge-Kutta (Orden 2)')
plt.title('Solución de f(x,y)=2xy con Runge-Kutta de segundo orden')
plt.xlabel('x')
plt.ylabel('y')
plt.legend()
plt.grid(True)
plt.show()

# Imprimir los resultados
for i in range(n+1):
    print(f"x = {x[i]:.4f}, y = {y[i]:.4f}")

# Calcular error
y_exact = -11.46
error = abs(y_exact - y[-1])
print(f"Error = {error:.4f}")

