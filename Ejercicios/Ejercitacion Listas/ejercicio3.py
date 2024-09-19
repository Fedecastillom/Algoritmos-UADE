#Crear una lista de N números generados al azar entre 
# 0 y 100 pero sin elementos repetidos. 
# El valor de N se ingresa por teclado. 
# Resolver este problema utilizando dos estrategias distintas:
#Impidiendo el agregado de elementos repetidos
# Eliminando los duplicados luego de generar la lista. Asegurarse que la 
# cantidad final de elementos sea la solicitada

import random

#Impidiendo el agregado de duplicados 
def generarListaAleatoriaSinRepetidos(N):
    lista=[]
    
    while len(lista)<N:
        numero= random.randint(0,100)
        
        presente=False
        contador=0
        while presente==False and contador<len(lista):
            if lista[contador]==numero:
                print("Encontro repetido: ",numero)
                presente=True
            contador+=1
        
        if not presente:
            lista.append(numero)
    
    return lista


#Eliminando duplicados 


def generarListaAleatoria(N):
    lista=[]
    while len(lista)<N:
        numero= random.randint(0,100)
        if numero==0:
            bandera=False
        else:
            lista.append(numero)
    return lista 

def eliminarDuplicados(lista):
    posInicial=0
    
    while posInicial<len(lista):
        posMasUno=posInicial+1
        while posMasUno<len(lista):
            if lista[posMasUno]==lista[posInicial]:
                del lista[posMasUno]
            else:
                posMasUno+=1
        posInicial+=1
    
    return lista 
                
        

print("Sin permitir duplicados desde el vamos")
cant=int(input("Ingrese la cantidad de numeros a generar\n "))

print(generarListaAleatoriaSinRepetidos(cant))


print("Duplicando luego de generar ")
lista= generarListaAleatoria(cant)
print("Lista original ",lista)

print("Lista sin repetidos: ", eliminarDuplicados(lista))
