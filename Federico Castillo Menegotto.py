import random

nombre = "Federico Castillo Menegotto"
lu = 1206075

def ejercicio1():
    print("[Ejercicio 1]")
    def temperaturas():
        return [random.randint(-10, 35) for _ in range(20)]
    
    def bajoCero(temperaturas):
        return [x for x in temperaturas if x < 0]
    
    def promedio(temperaturas):
        suma = 0
        for x in temperaturas:
            suma += x
        return suma / len(temperaturas)
    
    temperaturas = temperaturas()
    print(temperaturas)
    print(bajoCero(temperaturas))
    print(promedio(temperaturas))
    print(f"Desarrollado por {nombre}, {lu}\n")

def ejercicio2():
    print("[Ejercicio 2]")
    nombres = ["Federico","MACARENA","Francisco",
               "SANTINO","Matias","Sergio",
               "Andrea","Morena","Sofia","Candela"]
    
    def seleccionarNombres(nombres):
        vocales = "aeiouAEIOU"
        return [nombre for nombre in nombres if nombre[-1] in vocales]

    def insertionSort(nombres):
        for i in range(1, len(nombres)):
            j = i
            while j > 0 and nombres[j] < nombres[j-1]:
                nombres[j], nombres[j-1] = nombres[j-1], nombres[j]
                j -= 1
        return nombres
    
    nombresSeleccionados = seleccionarNombres(nombres)
    print(nombresSeleccionados)
    print(insertionSort(nombresSeleccionados))
    print(f"Desarrollado por {nombre}, {lu}\n")

def ejercicio3():
    print("[Ejercicio 3]")
    matriz1 = [[random.randint(5, 25) for _ in range(4)] for _ in range(4)]
    matriz2 = [[random.randint(5, 25) for _ in range(4)] for _ in range(4)]
    
    def restarMatrices(matriz1, matriz2):
        return [[matriz1[i][j] - matriz2[i][j] for j in range(4)] for i in range(4)]
    
    def diagonal(matriz):
        return [matriz[i][i] for i in range(4)]
    
    matriz3 = restarMatrices(matriz1, matriz2)
    
    print("Matriz 1:")
    for fila in matriz1:
        print(fila)
    
    print("\nMatriz 2:")
    for fila in matriz2:
        print(fila)
    
    print("\nMatriz 3:")
    for fila in matriz3:
        print(fila)
    
    print(f"\nDiagonal: {diagonal(matriz3)}")
    print(f"Desarrollado por {nombre}, {lu}\n")
    
def ejercicio4():
    print("[Ejercicio 4]")
    productos = [
        [1, "Pan", 600],
        [2, "Leche", 500],
        [3, "Harina", 250],
        [4, "Arroz", 400]
    ]
    
    print("\nProductos:")
    for producto in productos:
        print(producto)
    
    def precioVenta(productos):
        for producto in productos:
            aumento = round(producto[2] * 1.15)
            producto.append(aumento)
        return productos
    
    # def ordenarProductos(productos):
    #     for i in range(1, len(productos)):
    #         j = i
    #         while j > 0 and productos[j][2] > productos[j-1][2]:
    #             productos[j], productos[j-1] = productos[j-1], productos[j]
    #             j -= 1
    #     return productos
    
    def ordenarProductos(productos):
        for i in range(len(productos)):
            for j in range(len(productos) - 1):
                if productos[j][3] < productos[j + 1][3]:
                    productos[j], productos[j + 1] = productos[j + 1], productos[j]
        return productos
    
    productosOrdenados = ordenarProductos(precioVenta(productos))
    
    print("\nProductos ordenados + aumento:")
    for producto in productosOrdenados:
        print(producto)
    
    print(f"Desarrollado por {nombre}, {lu}\n")
    
ejercicio1()
ejercicio2()
ejercicio3()
ejercicio4()