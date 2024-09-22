nombre = "Federico Castillo Menegotto"
lu = 1206075

def ejercicio1():

    def descuento(x, y):
        return x * y

    precio_de_venta = int(input("Ingresar el precio de venta: "))
    if precio_de_venta > 30000:
        print(f"El precio con descuento es: {descuento(precio_de_venta, 0.95)}")
    elif precio_de_venta > 20000:
        print(f"El precio con descuento es: {descuento(precio_de_venta, 0.98)}")
    else:
        print("El precio ingresado no se le puede aplicar el descuento")
    
    print(f"Desarrollado por {nombre}, {lu}")

def ejercicio2():
    def es_mayor(x):
        return x >= 16

    carnets, menores, adultos, mayores = 0, 0, 0, 0
    while True:
        edad = int(input("Ingresar la edad de la persona (-1 para salir): "))
        if edad == -1:
            break
        elif not es_mayor(edad):
            menores += 1
        elif es_mayor(edad) and edad <= 80:
            carnets += 1
            adultos += 1
        elif edad > 80:
            mayores += 1
    
    print(f"El número de personas menores a 16 años es: {menores}\nEl número de personas entre 16 y 80 años es: {adultos}\nEl número de personas mayores a 80 años es: {mayores}")
    print(f"El numero total de carnets es: {carnets}")
    print(f"Desarrollado por {nombre}, {lu}")

def ejercicio3():
    def valor_aceptado(x):
        return (6000 <= x <= 50000)
    
    polizas, p6y30 , p30y40, p40y50 = 0, 0, 0, 0
    while polizas < 10:
        valor_poliza = int(input("Ingrese el valor de la poliza: "))
        if not valor_aceptado(valor_poliza):
            print("El valor de la poliza debe ser entre $6.000 y $50.000")
            continue
        elif 6000 <= valor_poliza <= 30000:
            p6y30 += 1
        elif 30000 < valor_poliza < 40000:
            p30y40 += 1
        elif valor_poliza >= 40000:
            p40y50 += 1
        polizas += 1
    print(f"Polizas entre $6.000 y $30.000: {p6y30}")
    print(f"Polizas mayores a $30.000 y menores a $40.000: {p30y40}")
    print(f"Polizas mayores o iguales a $40.000: {p40y50}")
    print(f"Desarrollado por {nombre}, {lu}")

