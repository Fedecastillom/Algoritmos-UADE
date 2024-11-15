import random

def ejercicio1():
    
    nombres = [random.randint(10,50) for _ in range(15)]
    
    def menorPar(nombres):
        menor = None
        for x in range(0, len(nombres), 2):
            if menor is None or nombres[x] < menor:
                menor = nombres[x]
        return menor
    
    def sumatoriaImpares(nombres):
        res = 0
        for x in range(1, len(nombres), 2):
            res += nombres[x]
        return res
    
    print(nombres)
    print(menorPar(nombres))
    print(sumatoriaImpares(nombres))

def ejercicio2():
    nombres = ["Federico","Macarena","Francisco",
               "Santino","Matias","Sergio",
               "Andrea","Morena","Sofia","Candela"]
    
    def seleccionarNombres(nombres):
        vocales = "aeiouAEIOU"
        return [x for x in nombres if x[-1] in vocales]
    
    def ordenarNombres(nombres):
        n = len(nombres)
        for i in range(n):
            for j in range(0, n - i - 1):
                if nombres[j] > nombres[j + 1]:
                    nombres[j], nombres[j + 1] = nombres[j + 1], nombres[j]
        return nombres
    
    def insertionSort(nombres):
        for i in range(1, len(nombres)):
            key = nombres[i]
            j = i - 1
            while j >= 0 and nombres[j] > key:
                nombres[j + 1] = nombres[j]
                j -= 1
            nombres[j + 1] = key
        return nombres
    
    print(seleccionarNombres(nombres))
    print(ordenarNombres(seleccionarNombres(nombres)))
    print(insertionSort(seleccionarNombres(nombres)))
    
def ejercicio3():
    matriz1 = [[random.randint(10, 50) for _ in range(5)] for _ in range(5)]
    matriz2 = [[random.randint(10, 50) for _ in range(5)] for _ in range(5)]
    
    def multiplicarMatriz(matriz1, matriz2):
        return [[matriz1[i][j] * matriz2[i][j] for j in range(5)] for i in range(5)]

    def diagonal(matriz):
        return [matriz[i][len(matriz) - i - 1] for i in range(len(matriz))]
    
    print(matriz1)
    print(matriz2)
    print(multiplicarMatriz(matriz1, matriz2))
    print(diagonal(multiplicarMatriz(matriz1, matriz2)))
    
def ejercicio4():
    ventas = [
    [1, "Carne", 10, 300],
    [2, "Fideos", 5, 200],
    [3, "Chocolate", 8, 500],
    [4, "Galletita", 15, 100],
    [5, "Pan", 3, 150],
    [6, "Leche", 12, 230]
    ]
    
    def totalVendido(ventas):
        for venta in ventas:
            venta.append(venta[2] * venta[3])
        return ventas
    
    def selectionSort(matriz):
        for i in range(len(matriz)):
            minimo = i
            for j in range(i + 1, len(matriz)):
                if matriz[j][1] < matriz[minimo][1]:
                    minimo = j
            matriz[i], matriz[minimo] = matriz[minimo], matriz[i]
        return matriz
    
    res = selectionSort(totalVendido(ventas))
    for x in res:
        print(x)
    