import matplotlib.pyplot as plt


#EJERCIO APLICANDO EULER
def euler(f,x,y,h,m):
    u = []
    v = []
    for i in range(m):
        y = y + h*f(x,y)
        x = x + h
        u.append(x)
        v.append(y)
    return u,v

def f(x,y):
    '''Aqui añadimos la EDO'''
    return (1+4*x*y) / (3*x**2) #Esto se modifica


x = 0.5 #Esto se modifica
y = -1 #Esto se modifica
h = 0.035 #Esto se modifica
m = 100 #Esto se modifica
u,v = euler(f,x,y,h,m)

print(v[-1])

def error(v,v_aprox):
    return abs(v-v_aprox)

print('Error: ', error(-11.46,v[-1]))

#Grafica
plt.plot(u,v,label='Euler')
plt.xlabel('x')
plt.ylabel('y')
plt.legend()
plt.show()

