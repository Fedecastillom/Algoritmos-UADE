def ejercicio1():
    harinaGr = int(input("Ingrese la cantidad de harina en gramos: "))
    azucarGr = int(input("Ingrese la cantidad de azucar en gramos: "))
    mantecaGr = int(input("Ingrese la cantidad de manteca en gramos: "))

    lotesMax = min(harinaGr // 250, azucarGr // 150, mantecaGr // 100)
    harinaSobrante = harinaGr - (lotesMax * 250)
    azucarSobrante = azucarGr - (lotesMax * 150)
    mantecaSobrante = mantecaGr - (lotesMax * 100)

    return lotesMax, harinaSobrante, azucarSobrante, mantecaSobrante

def ejercicio2():
    def es_divisible(x, y):
        return x % y == 0

    x = int(input("Ingrese un numero entre 5 y 15: "))
    while x < 5 or x > 15:
        print("El numero debe estar entre 5 y 15")
        x = int(input("Ingrese un numero entre 5 y 15: "))
    
    cantDivisibles, mayor, menor = 0, None, None
    while True:
        num = int(input("Ingrese numeros enteros positivos (-1 para salir): "))
        if num == -1:
            break
        elif num < -1:
            print("El numero ingresado debe ser positivo")
            continue

        if es_divisible(num, x):
            print(f"{num} es divisible por {x}")
            cantDivisibles += 1
            if mayor is None or num > mayor:
                mayor = num
            if menor is None or num < menor:
                menor = num
        else:
            print(f"{num} no es divisible por {x}")
    return cantDivisibles, mayor, menor

def ejercicio3():
    def promedio(x, y):
        return round(x / y, 2) if total > 0 else 0
    
    total, catA, catB, catC = 0, 0, 0, 0
    YearsCatA, YearsCatB, YearsCatC = 0, 0, 0
    
    while True:
        year = int(input("Ingrese los años de servicio del empleado (-1 para salir): "))
        if year == -1:
            break
        elif year < -1:
            print("El año de servicio debe ser positivo")
            continue
        if 1 <= year <= 5:
            catA += 1
            YearsCatA += year
        elif 6 <= year <= 10:
            catB += 1
            YearsCatB += year
        elif year >= 11:
            catC += 1
            YearsCatC += year
        total += 1
    print(f"Cantidad total de empleados: {total}")
    print(f"Cantidad de empleados Categoria A: {catA}. Promedio: {promedio(YearsCatA, total)}")
    print(f"Cantidad de empleados Categoria B: {catB}. Promedio: {promedio(YearsCatB, total)}")
    print(f"Cantidad de empleados Categoria C: {catC}. Promedio: {promedio(YearsCatC, total)}")
    return catA, catB, catC

ejercicio3()