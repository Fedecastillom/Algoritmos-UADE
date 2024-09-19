#Ejercicio 2
def sumar_lista(lista):
    suma = 0
    for num in lista:
        suma += num
    return suma

#Ejercicio 3
def maximo_lista(lista):
    maximo = lista[0]
    for num in lista:
        if num > maximo:
            maximo = num
    return maximo

#Ejercicio 4
def busqueda_secuencial(lista, valor):
    for i in range(len(lista)):
        if lista[i] == valor:
            return i
    return -1

#Ejercicio 5 
def orden_seleccion(lista):
    largo = len(lista)
    for i in range(largo-1):
        for j in range(i+1, largo):
            if lista[i] > lista[j]:
                aux=lista[i]
                lista[i]=lista[j]
                lista[j]=aux
    return lista 

#Ejercicio 6:
def revertir_lista(lista):
    invertida = []
    for i in range(len(lista)-1, -1, -1):
        invertida.append(lista[i])
    return invertida


#Ejercicio 7:
def segundo_mayor(lista):
    if len(lista) < 2:
        return None
    
    maximo = lista[0]
    posicion=0

    for num in range(len(lista)):
        if lista[num] > maximo:
            maximo=lista[num]
            posicion=num
            
    del lista[posicion]
    
    segundo_maximo=lista[0]
    
    for x in range(len(lista)):
        if lista[x] > segundo_maximo:
            segundo_maximo=lista[x]
            
    
    return segundo_maximo 



# Crear una lista vacía y agregar números del 1 al 10
numeros = []
for i in range(1, 11):
    numeros.append(i)

print(numeros) 


# Ejercicio 2 
print(sumar_lista(numeros))  


#Ejercicio 3:
print(maximo_lista(numeros))


#Ejercicio 4:
print(busqueda_secuencial(numeros, 5))  # 4
print(busqueda_secuencial(numeros, 11))  # -1


#Ejercicio 5:
print(orden_seleccion([9,7,6,3,2,55]))


# Ejercicio 7
print(segundo_mayor([10, 5, 20, 8, 15]))  
