
#Rellenar una lista con números enteros entre 0 y 100 obtenidos al azar e imprimir el valor mínimo y el lugar que ocupa. Tener en cuenta que el mínimo puede 
#estar repetido, en cuyo caso deberán mostrarse todas las posiciones en las que  se encuentre. La carga de datos termina cuando se obtenga un 0 como número 
#al azar, el que no deberá cargarse en la lista
import random

def generarListaAleatoria():
    lista=[]
    bandera=True
    while bandera:
        numero= random.randint(0,100)
        if numero==0:
            bandera=False
        else:
            lista.append(numero)
    return lista 


def buscarMinimo(lista):
    minimo=None
    posiciones=[]
    
    for i in range(len(lista)):
        if minimo==None or lista[i]<minimo:
            minimo=lista[i]
    
    for i in range(len(lista)):
        if lista[i]==minimo:
            posiciones.append(i)
    
    return minimo,posiciones

lista=generarListaAleatoria()

print(buscarMinimo(lista))

