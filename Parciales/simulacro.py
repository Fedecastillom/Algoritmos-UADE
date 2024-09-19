# Escribir un programa para ingresar por teclado los años de antigüedad de cada socio de un
# club.
# El club posee 3 categorías, dependiendo de la cantidad de años que tenga cada socio.
# Categoría 1 (1 a 12 años de antigüedad)
# Categoría 2 (13 a 25 años de antigüedad)
# Categoría 3 (26 años o más).
# El fin de los datos se indica ingresando -1.
# Se solicita imprimir un informe que contenga:
# - Cantidad total de personas que son socios del club.
# - Cantidad de socios por categoría.
# - Promedio de antigüedad de todos los socios de cada categoría

def socios():
    club = {
        "categoria 1": {"socios": 0, "antiguedad":0},
        "categoria 2": {"socios": 0, "antiguedad":0},
        "categoria 3": {"socios": 0, "antiguedad":0}
    }

    total_socios = 0

    while True:
        entrada = input("Ingrese la antigüedad del socio (-1 para finalizar): ")
        if entrada == "":
            print("Valor invalido")
            continue

        antiguedad = int(entrada)
        if antiguedad == -1:
            break
        
        elif antiguedad < 0:
            print("Valor invalido")
        
        elif 1 <= antiguedad <= 12:
            club["categoria 1"]["socios"] += 1
            club["categoria 1"]["antiguedad"] += antiguedad
            total_socios += 1
        
        elif 13 <= antiguedad <= 25:
            club["categoria 2"]["socios"] += 1
            club["categoria 2"]["antiguedad"] += antiguedad
            total_socios += 1

        elif 26 <= antiguedad:
            club["categoria 3"]["socios"] += 1
            club["categoria 3"]["antiguedad"] += antiguedad
            total_socios += 1

    if total_socios > 0:
        print(f"\nTotal de socios: {total_socios}\n")
        for categoria, datos in club.items():
            cantidad_socios = datos["socios"]
            
            if cantidad_socios > 0:
                promedio_antiguedad = datos["antiguedad"] / cantidad_socios
                print(f"[{categoria}]\nSocios: {cantidad_socios}\nPromedio antiguedad: {promedio_antiguedad:.1f}\n")
            else:
                print(f"No hay socios en la {categoria}\n")

    else:
        print("\nNo hay socios en el club\n")

# Un pastelero sabe que cada chocotorta requiere 500 grs de galletitas de chocolate, 400 grs
# de dulce de leche y 180 grs de queso crema.
# Desarrollar un programa que lea por teclado la cantidad de cada ingrediente en kilos e
# informar cuántas chocotortas pueden prepararse, y cuánto de cada ingrediente sobra al
# final.

def chocotorta():
    galletitas_kg = float(input("Ingrese la cantidad de galletitas en KG: "))
    dulce_kg = float(input("Ingrese la cantidad de dulce de leche en KG: "))
    queso_kg = float(input("Ingrese la cantidad de queso en KG: "))

    galletitas_grs = galletitas_kg * 1000
    dulce_grs = dulce_kg * 1000
    queso_grs = queso_kg * 1000

    chocotortas_galletitas = galletitas_grs // 500
    chocotortas_dulce = dulce_grs // 400
    chocotortas_queso = queso_grs // 180

    chocotortas_posibles = min(chocotortas_galletitas, chocotortas_dulce, chocotortas_queso)

    galletitas_sobrantes = galletitas_grs - (chocotortas_posibles * 500)
    dulce_sobrantes = dulce_grs - (chocotortas_posibles * 400)
    queso_sobrantes = queso_grs - (chocotortas_posibles * 180)

    print(f"Se pueden preparar {chocotortas_posibles} chocotortas")
    print(f"Con {galletitas_sobrantes} gramos de galletitas sobrantes")
    print(f"Con {dulce_sobrantes} gramos de dulce de leche sobrantes")
    print(f"Con {queso_sobrantes} gramos de queso crema sobrantes")

# Se solicita realizar un programa que lea un número por teclado.
# Dicho número, que deberá estar entre 2 y 9, será utilizado por el programa como múltiplo.
# Una vez que se conoce el múltiplo, se deberá solicitar ahora por teclado la carga de
# números enteros positivos, terminando la carga con -1.
# Se solicita lo siguiente:
# - A cada número ingresado, indicar si es o no múltiplo.
# - Devolver la cantidad total de números ingresados que son múltiplos del primero.
# - Indicar el múltiplo mayor y el múltiplo menor ingresado.

def multiplo():
    numeros = []
    multiplos = []
    no_multiplos = []
    while True:
        m = int(input("Ingrese un numero entre 2 y 9: "))
        if m < 2 or m > 9:
            print("El numero debe estar entre 2 y 9.")
            continue
        break
    
    while True:
        n = int(input("Ingrese un numero entero positivo (-1 para finalizar): "))
        if n == -1:
            break

        elif n < 0:
            print("El numero debe ser positivo.")
            continue
        
        numeros.append(n)
    
    for k in numeros:
        if k % m == 0:
            multiplos.append(k)
        else:
            no_multiplos.append(k)
    
    print(f"Cantidad total de numeros ingresados: {len(numeros)}, cantidad de multiplos ingresados: {len(multiplos)}")
    print(f"Los numeros multiplos de {m} son {multiplos}\nLos numeros no multiplos de {m} son {no_multiplos}")
    print(f"El multiplo menor es: {min(multiplos)} y el multiplo mayor es: {max(multiplos)}")
