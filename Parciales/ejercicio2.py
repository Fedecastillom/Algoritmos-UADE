"""Escribir un programa para ingresar tres números naturales que corresponden a las
longitudes de tres segmentos e informar si conforman un triángulo y si lo hacen, de qué tipo
es.
Para ello se deberá:
a. Ingresar la longitud de cada segmento. Verificar que sean naturales.
b. Verificar que los tres lados conformen un triángulo (ver teorema).
c. En caso de haberse comprobado que es posible formar un triángulo, informar si el
triángulo es equilátero (tres lados iguales), isósceles (dos lados iguales) o escaleno (todos
los lados diferentes).
Teorema de la desigualdad del triángulo: Este teorema simplemente establece que la
suma de dos de los lados del triángulo debe ser mayor al tercer lado. Si esto es verdad en
todas las combinaciones (tres), entonces es un triángulo."""

def es_natural(n):
    return n > 0

def es_triangulo(a, b, c):
    return (a + b > c) and (a + c > b) and (b + c > a)

def solucion():
        a = int(input("Ingresar segmento A: "))
        b = int(input("Ingresar segmento B: "))
        c = int(input("Ingresar segmento C: "))
        for segmento in [a, b, c]:
            if not es_natural(segmento):
                print("ERROR -- Ingresar solo numeros naturales.")
                break
        if es_triangulo(a, b, c):
            if a == b == c:
                print("Es un triangulo equilatero")
            elif (a == b or a == c or b == c) and not (a == b == c):
                print("Es un triángulo isósceles")
            else:
                print("Es un triangulo escaleno")
        else:
            print("Los valores ingresados no cumplen con el teorema")
