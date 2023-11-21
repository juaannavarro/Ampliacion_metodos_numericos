import matplotlib.pyplot as plt


#EJERCIO 1
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
    return y-x**2+1


x = 0
y = 0.5
h = 0.025
m = 20
u,v = euler(f,x,y,h,m)



x1=0
y1=0
h1=0.025
m1=20
u1,v1=euler(f,x1,y1,h1,m1)


x2=0
y2=-1
h2=0.025
m2=20
u2,v2=euler(f,x2,y2,h2,m2)


plt.plot(u,v)
plt.plot(u1,v1)
plt.plot(u2,v2)
plt.grid(True)
plt.show()







