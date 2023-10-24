def polinomio_taylor(x,y,h,n):
    for i in range(1,n+1):
        y = y + h*funcion(x,y)
        x = x + h
    return y

def funcion(x,y):
    return (2-x-y)/(x-y+4)

def h(a,b,n):
    return (b-a)/n

def main():
    a=int(input("Ingrese el valor de a: "))
    b=int(input("Ingrese el valor de b: "))
    n=int(input("Ingrese el valor de n: "))
    x=int(input("Ingrese el valor de x: "))
    y=int(input("Ingrese el valor de y: "))
    h=h(a,b,n)
    polinomio_taylor(x,y,h,n)
    print("El valor de y es: ",y)
