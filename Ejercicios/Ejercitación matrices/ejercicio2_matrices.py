import random
#Sumar los elementos de una matriz de 2 x 2
#Crear una matriz de dos por dos con números aleatorios de 0 a 9
#2) Sumar todos esos elementos e imprimir la suma 

matriz_dos_por_dos=[]
suma=0
for f in range(2):
    fila=[]
    for c in range(2):
        valor= random.randint(0,9)
        fila.append(valor)
        suma+=valor
    matriz_dos_por_dos.append(fila)

print(matriz_dos_por_dos)
print("La suma de los elementos de la matriz es: ",suma)
