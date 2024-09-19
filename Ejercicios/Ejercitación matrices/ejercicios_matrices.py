#Crear una matriz de 3 x 3, y la tenemos que llenar con números del 1 al 9. 
#Luego que imprimir la matriz 

matriz=[]
contador=1

for fila in range(3):
    fila=[]
    for columna in range(3):
        fila.append(contador)
        contador+=1
    matriz.append(fila)

for fila in range(len(matriz)):
    for columna in range(len(matriz[fila])):
        print(matriz[fila][columna], end=" ")
    print()



