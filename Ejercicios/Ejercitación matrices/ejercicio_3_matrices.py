#Multiplicar una matriz de 3x3 por un número que ingrese el usuario 

matriz_cuatro_x_cuatro=[]
matriz_cuatro_x_cuatro.append([5,4,3,2])
matriz_cuatro_x_cuatro.append([8,9,12,34])
matriz_cuatro_x_cuatro.append([55,44,33,22])
matriz_cuatro_x_cuatro.append([4,5,6,7])

numero= int(input("Ingrese el valor por el que se va a multiplicar la matriz\n"))

print("Matriz antes de multiplicar por un número\n")
for fila in range(len(matriz_cuatro_x_cuatro)):
    for columna in range(len(matriz_cuatro_x_cuatro[fila])):
        print(matriz_cuatro_x_cuatro[fila][columna], end=" ")
    print()
    
print("Matriz luego de multiplicar por un escalar")
for f in range(len(matriz_cuatro_x_cuatro)):
    for c in range(len(matriz_cuatro_x_cuatro[f])):
        matriz_cuatro_x_cuatro[f][c]*=numero
        print(matriz_cuatro_x_cuatro[f][c], end=" ")
    print()
        


        