import math

def area_triangulo(base, altura):
    return (base + altura) / 2

def perimetro(longitud, ancho):
    return 2 * (longitud + ancho)

def fuerza(masa, aceleracion):
    return masa * aceleracion

def distancia():
    x1 = int(input("Ingrese X1:"))
    y1 = int(input("Ingrese y1:"))
    x2 = int(input("Ingrese x2:"))
    y2 = int(input("Ingrese y2:"))
    return round(math.sqrt((x2 - x1)**2 + (y2 - y1)**2))