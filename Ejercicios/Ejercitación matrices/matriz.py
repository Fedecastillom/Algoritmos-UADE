#Creamos una matriz 
filas = int(input("Ingrese la cantidad de filas que desee que tenga nuestra matriz\n"))
columnas = int(input("Ingrese la cantidad de columnas que desee que tenga nuestra matriz\n"))
matriz=[]
for fila in range(filas):
    matriz.append([])
    for columna in range(columnas):
        matriz[fila].append(0)
print(matriz)

#Recorrer la matriz y modificar los números 
for fila in range(filas):
    for columna in range(columnas):
        valor= int(input("Ingrese un valor\n"))
        matriz[fila][columna]=valor
print(matriz)

#Imprimir en formato de matriz
for fila in range(filas):
    for columna in range(columnas):
        print(matriz[fila][columna], end=" ")
    print()