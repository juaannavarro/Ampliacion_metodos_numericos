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
    return (x+y)/(x-y)


x = -4
y = 4
h = 0.04
m = 100
u,v = euler(f,x,y,h,m)

print(v[-1])