#Cargar dos listas de números A y B con N números al azar entre 1 y 100, 
# donde N se ingresa por teclado. Mostrar ambas listas por pantalla. 
# Luego construir e  imprimir tres nuevas listas C, D y E que contengan:
#· La concatenación de los valores pares de A con los impares de B. 
# (valores pares o valores impares se refiere a los elementos propiamente 
# dichos y no a sus posiciones).
#· La concatenación de los valores impares de A con el reverso de  los valores pares de B. 
#· La intercalación de los elementos de A y B

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

#· La concatenación de los valores pares de A con los impares de B. 
# (valores pares o valores impares se refiere a los elementos propiamente 
# dichos y no a sus posiciones).
def concatenarValoresParesImpares(listaUno, listaDos):
    lista=[]
    
    for i in range(len(listaUno)):
        if listaUno[i]%2==0:
            lista.append(listaUno[i])
    
    for i in range(len(listaDos)):
        if listaDos[i]%2!=0:
            lista.append(listaDos[i])
    return lista 

# La concatenación de los valores impares de A con el reverso de  los valores pares de B. 
def concatenarImparesyReverso(listaUno,listaDos):
    lista=[]
    
    for i in range(len(listaUno)):
        if listaUno[i]%2!=0:
            lista.append(listaUno[i])
            
    for i in range(len(listaDos)-1,-1,-1):
        lista.append(listaDos[i])
    
    return lista

def intercalarListas(listaUno,listaDos):
    lista=[]
    largoMinimo=0
    
    if (len(listaUno)>=len(listaDos)):
        largoMinimo=len(listaDos)
    else:
        largoMinimo=len(listaUno)
    
    for i in range(largoMinimo):
        lista.append(listaUno[i])
        lista.append(listaDos[i])

    if len(listaUno)>largoMinimo:
        for i in range(largoMinimo,len(listaUno)):
            lista.append(listaUno[i])
    else:
        for i in range(largoMinimo,len(listaDos)):
            lista.append(listaDos[i])
    
    return lista

#Programa Principal 
lista1=generarListaAleatoria()
print("Lista Uno")
print(lista1)

print("Lista Dos")
lista2=generarListaAleatoria()
print(lista2)

print("Concatenada")
print(concatenarValoresParesImpares(lista1,lista2))

print("Lista Impares y reversa")
print(concatenarImparesyReverso(lista1,lista2))            

print("Intercalado")
print(intercalarListas(lista1,lista2))
