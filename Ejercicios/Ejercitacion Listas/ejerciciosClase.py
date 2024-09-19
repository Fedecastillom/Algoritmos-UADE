import random

# 1) Crear una lista vacia y agregar números del 1 al 10 usando un bucle for

def crearLista():
    lista=[]
    for i in range(1,11):
        lista.append(i)
    return lista

# 2) Realizar una función que sume todos los valores de una lista

def sumarLista(lista):
    suma=0
    for i in range(len(lista)):
        suma+=lista[i]
    return suma 

# 3) Realizar una función que informe el máximo de una lista
def determinarMaximo(lista):
    max=lista[0]
    for i in range(len(lista)):
        if lista[i]>max:
            max=lista[i]
    return max
            
# 4) Implementar una función que busque un valor en la lista y retorne su índice o -1 si no se encuentra

def buscarElemento(lista,elemento):
    for i in range(len(lista)):
        if lista[i]==elemento:
            return  i
    return -1
    
    

# 5) Implementar una función que ordene una lista con el algoritmo de selección
def ordenarListaPorSeleccion(lista):
    for i in range(len(lista)-1):
        for j in range(i+1,len(lista)):
            if lista[i]>lista[j]:
                aux=lista[i]
                lista[i]=lista[j]
                lista[j]=aux 
    return lista 

# 6) Implementar una función que revierta una lista 

def revertirLista(lista):
    invertida=[]
    for i in range(len(lista)-1,-1,-1):
        invertida.append(lista[i])
    return invertida
# 7) Encontrar el segundo mayor número en una lista 
def determinarSegundoMaximo(lista):
    if len(lista)<2:
        return -1 
    max=lista[0]
    for i in range(len(lista)):
        if lista[i]>max:
            max=lista[i]
    segundoMaximo=lista[0]
    for x in range(len(lista)):
        if lista[x]>segundoMaximo and lista[x]<max:
            segundoMaximo=lista[x]
    return segundoMaximo
        
def determinarSegundoMaximoOp2(lista):
    if len(lista)<2:
        return -1 
    
    for i in range(len(lista)-1):
        for j in range(i+1,len(lista)):
            if lista[i]>lista[j]:
                aux=lista[i]
                lista[i]=lista[j]
                lista[j]=aux 
    maximo=lista[len(lista)-1]
    posicion=0
    for i in range(len(lista)-1):
        if lista[i]!=maximo:
            posicion=i
    segundoMaximo=lista[posicion]
    return segundoMaximo
    
#Rellenar una lista con números enteros entre 0 y 100 obtenidos al azar e imprimir el valor mínimo y el lugar que ocupa. Tener en cuenta que el mínimo puede 
#estar repetido, en cuyo caso deberán mostrarse todas las posiciones en las que  se encuentre. La carga de datos termina cuando se obtenga un 0 como número 
#al azar, el que no deberá cargarse en la lista

def generarListaAleatoria():
    lista=[]
    bandera=True
    while bandera:
        numero=random.randint(0,100)
        if numero==0:
            bandera=False
        else:
            lista.append(numero)
    return lista

def determinarMinimo(lista):
    posiciones=[]
    minimo=None 
    for i in range(len(lista)):
        if minimo==None or lista[i]<minimo:
            minimo=lista[i]
    for i in range(len(lista)):
        if minimo==lista[i]:
            posiciones.append(i)
    return minimo,posiciones
    
    
##Crear una lista de N números generados al azar entre 
# 0 y 100 pero sin elementos repetidos. 
# El valor de N se ingresa por teclado. 
# Resolver este problema utilizando dos estrategias distintas:
#Impidiendo el agregado de elementos repetidos
# Eliminando los duplicados luego de generar la lista. Asegurarse que la 
# cantidad final de elementos sea la solicitada

def generarListaAleatoriaSinRepVer1(n):
    lista=[]
    if n>100:
        return -1 
    else:
        while len(lista)<n:
            numero=random.randint(0,100)
            repetido=False
            contador=0
            while repetido==False and contador<len(lista):
                if numero==lista[contador]:
                    repetido=True
                contador+=1
            if repetido==False:
                lista.append(numero)
    return lista 
                     
       
            

    

#Programa principal
#Invocación Ejercicio 1 
print("Ejercicio 1")
lista=crearLista()
print(lista)

#Invocación Ejercicio 2
print("Ejercicio 2")
print(sumarLista(lista))

#Invocación Ejercicio 3
print("Ejercicio 3")
print(determinarMaximo(lista))

#Invocación Ejercicio 4
print("Ejercicio 4")
print(buscarElemento(lista,4))

#Invocación Ejercicio 5
print("Ejercicio 5")
print(ordenarListaPorSeleccion([7,6,66,55,44,33,22,109]))


#Invocación Ejercicio 6
print("Ejercicio 6")
print(revertirLista([7,6,66,55,44,33,22,109]))

#Invocación Ejercicio 7
print("Ejercicio 7")
print(determinarSegundoMaximo([7,6,66,55,44,109,33,22,109]))
print(determinarSegundoMaximoOp2([7,6,66,55,44,109,33,22,109]))

#Invocación Ejercicio 8 (Guia de Listas)
print("Ejercicio 8")
lista=generarListaAleatoria()
print(lista)
print("Minimo y posiciones ",determinarMinimo(lista))


#Invocación Ejercicio 9 (Guia de Listas)
print("Ejercicio 9")
cant=int(input("Ingrese la cantidad de elementos de la lista\n"))
print(generarListaAleatoriaSinRepVer1(cant))