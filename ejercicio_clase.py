import matplotlib.pyplot as plt
import math as ma

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
    return 2*x*ma.exp(-3*x)-3*y

x=0
y=1
h=0.1
m=20
u,v=euler(f,x,y,h,m)



x2=-0.65
y2=0
h2=0.1
m2=40
u2,v2=euler(f,x2,y2,h2,m2)




plt.plot(u,v)

plt.plot(u2,v2)


plt.show()
