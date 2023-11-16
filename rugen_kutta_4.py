import numpy as np
import matplotlib.pyplot as plt

# Definir la función
def f(x, y):
    return (1 + 4*x*y)/(3*x**2)

# Método de Runge-Kutta de cuarto orden
def runge_kutta(x0, y0, xn, n):
    h = (xn-x0)/float(n)
    x = np.linspace(x0, xn, n+1)
    y = np.zeros(n+1)
    y[0] = y0
    for i in range(n):
        k1 = h * f(x[i], y[i])
        k2 = h * f(x[i] + 0.5*h, y[i] + 0.5*k1)
        k3 = h * f(x[i] + 0.5*h, y[i] + 0.5*k2)
        k4 = h * f(x[i] + h, y[i] + k3)
        y[i+1] = y[i] + (k1 + 2*k2 + 2*k3 + k4)/6
    return x, y

# Parámetros
x0 = 0.5
y0 = -1
xn = 4
n = 100

# Calcular y trazar la solución
x, y = runge_kutta(x0, y0, xn, n)
plt.plot(x, y, 'o-', label='Runge-Kutta')
plt.title('Solución de f(x,y)=2xy con Runge-Kutta')
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

