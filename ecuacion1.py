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
    return (2-x-y)/(x-y+4)


x = -2
y = 0
h = 0.1
m = 20
u,v = euler(f,x,y,h,m)



x1=0
y1=2
h1=0.1
m1=20
u1,v1=euler(f,x1,y1,h1,m1)


x2=2
y2=4
h2=0.1
m2=20
u2,v2=euler(f,x2,y2,h2,m2)

x3=-3
y3=4
h3=0.1
m3=20
u3,v3=euler(f,x3,y3,h3,m3)


plt.plot(u,v)
plt.plot(u1,v1)
plt.plot(u2,v2)
plt.plot(u3,v3)
plt.show()








