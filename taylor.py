import matplotlib.pyplot as plt

# Método de Taylor de orden 2
def taylor_order_2(f, df_dx,df_dy, x, y, h, m):
    u = []
    v = []
    for i in range(m):
        # Taylor de orden 2
        y = y + h * f(x, y) + (0.5 * h**2)*( df_dx(x, y)+ f(x, y) * df_dy(x, y))
        x = x + h
        u.append(x)
        v.append(y)
    return u, v

# Función y su derivada respecto a x
def f(x, y):
    return (1 + 4 * x * y) / (3 * x**2)

def df_dx(x, y):
    return-(4*x*y+2/3*x**3)
def df_dy(x, y):
    return 4 / (3 * x) 

x = 0.5
y = -1
h = 0.035
m = 100

u, v = taylor_order_2(f, df_dx,df_dy, x, y, h, m)

print(v[-1])

# Error
def error(v, v_aprox):
    return abs(v - v_aprox)

print('Error:', error(-11.46, v[-1]))

# Gráfico
plt.plot(u, v, label='Taylor de orden 2')
plt.xlabel('x')
plt.ylabel('y')
plt.legend()
plt.show()
