def ejemplo_1():
    importe = int(input("Ingrese el importe de la venta: $"))
    return importe * (0.95 if importe >= 30000 else 0.98)

def ejemplo_2():
    importe = int(input("Ingrese el importe de la venta: $"))
    score = int(input("Ingrese el score del cliente: "))
    return importe * (0.95 if importe >= 30000 and score > 20 else 0.98)

def ejemplo_3():
    importe = int(input("Ingrese el importe de la venta: $"))
    score = int(input("Ingrese el score del cliente: "))
    if importe >= 30000 and score > 20:
        return importe * 0.95
    elif importe >= 10000 or score > 10:
        return importe * 0.98
    else:
        return importe
    
def ejercicio_1():
    x = int(input("Ingrese un numero: "))
    return x if x > 10 else None
    
def ejercicio_2():
    x = int(input("Ingrese un numero: "))
    if x > 0:
        print("Es positivo")
    elif x < 0:
        print("Es negativo")
    else:
        print("Es neutro")

def ejercicio_3():
    x = int(input("Ingrese una calificacion: "))
    if x >= 90:
        print("A")
    elif x >= 80:
        print("B")
    elif x >= 70:
        print("C")
    elif x >= 60:
        print("D")
    else:
        print("F")

def ejercicio_4():
    x = int(input("Ingrese su edad: "))
    y = int(input("Ingrese su peso en KG: "))
    if x >= 18 and x <= 65 and y >= 50:
        print("Puede donar sangre")
    else:
        print("No puede donar sangre")

def ejercicio_5():
    x = int(input("Ingrese la temperatura exterior en Celcius: "))
    y = int(input("Ingrese la velocidad del viento: "))
    if x < 0 or y >= 60:
        print("Es peligroso salir!!")
    else:
        print("Es seguro salir")

def ejercicio_6():
    x = int(input("Ingrese un numero: "))
    if x % 5 == 0:
        print("Es divisible por 5")
    else:
        print("No es divisible por 5")

def ejercicio_9():
    x = int(input("Ingrese las hs trabajadas: "))
    y = int(input("Ingrese la paga por hora: "))
    return "Recibe pago extra" if x > 40 and y >= 20 else "Pago Insuficiente" if x < 40 and y < 10 else "Pago adecuado"
