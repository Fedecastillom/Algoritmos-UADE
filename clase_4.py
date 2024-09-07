def ejercicio_1():
    lista = []
    pares = []
    i = 0
    while i < 10:
        num = int(input("Ingrese un número: "))
        if num > 10:
            lista.append(num)
        if num%2 == 0 and (20 <= num <= 30):
            pares.append(num)
        else:
            pass
        i += 1
    return lista, pares

def ejercicio_3():
    lista = []
    while True:
        num = int(input("Ingrese un número: "))
        if num == 0:
            break
        elif num < 50:
            lista.append(num)
    return len(lista)

def ejercicio_4():
    lista = []
    while True:
        num = int(input("Ingrese un número: "))
        if num == 0:
            break
        lista.append(num)
    return sum(lista) / len(lista)

def ejercicio_5():
    list = []
    i = 10
    while i > 0:
        list.append(i)
        i -= 1
    return list

def fibonacci(n):
    lista = [0, 1]
    while len(lista) < n:
        lista.append(lista[-1] + lista[-2])
    return lista

def fibonacci_of(n):
    if n in {0, 1}:
        return n
    return fibonacci_of(n - 1) + fibonacci_of(n - 2)

def ejercicio_6():
    x = 0
    y = 0
    while True:
        num = int(input("Ingrese un numero: "))
        if num == 0:
            break
        x += num
        y += 1
    return x / y