import matplotlib.pyplot as plt
import numpy as np

def euler2(f, x, u, v, h, n, m):
    r = []
    t = []
    for i in range(n):
        x = x + h
        u = u + h * v
        v = v + h * f(x, u, v, m)
        r.append(x)
        t.append(u)
    return r, t

def f(x, u, v,m): #la m sale de la ecuacion de Bessel
    '''Aqui definimos la EDO de segundo orden (se despeja la y'')'''
    return ((np.exp(-2*x))/(1-x**2))-4*v-4*u

# Datos
m=1
x_inicial = -0.99
x_final = 1
x = -0.99
u = 0 #recodar que la u es la y
v = 1 #es y'
n = 100
h = (x_final - x_inicial) / n
m=1 #para la ecuacion de Bessel





# Método de Euler de segundo orden 
r, t = euler2(f, x, u, v, h, n,m)



# Gráfica
plt.plot(r, t, label='Solución numérica')
plt.xlabel('x')
plt.ylabel('u(x)')
plt.title('Bessel')
plt.legend()
plt.grid(True)
plt.show()
plt.savefig('grafica3.png')


