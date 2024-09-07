def hello():
    return "hello world"

def sum2(x, y):
    return x + y

def temp(x):
    return x * 9/5 + 32

def area(x, y):
    return x * y

def swap(x, y):
    aux = y
    y = x
    x = aux
    return x, y

def prom():
    list = []
    while len(list) < 3:
        x = int(input("Ingrese un valor: "))
        list.append(x)
    return sum(list) / len(list)

def radio(x):
    return 3.14 * x * x

def hours(x):
    horas, minutos = divmod(x, 60)
    return f"Son {horas}hs con {minutos}m"

def age(x):
    year = 2024
    return year - x

def compra(x, y):
    return x - (x * y / 100)

def bisiesto(year):
    if year%4 != 0:
        return False
    elif year%100 == 0 and year%400 != 0:
        return False
    else:
        return True