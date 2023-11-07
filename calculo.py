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
    return (2-3*x-y)/(x-1)


x = 2
y = -1
h = 0.02
m = 200
u,v = euler(f,x,y,h,m)

print(v[-1])