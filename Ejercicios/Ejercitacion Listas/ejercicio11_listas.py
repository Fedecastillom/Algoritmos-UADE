import random
#Cargar dos listas de números A y B con N números al azar entre 1 y 100, 
# donde N se ingresa por teclado. Mostrar ambas listas por pantalla. 
# Luego construir e  imprimir tres nuevas listas C, D y E que contengan:
#· La concatenación de los valores pares de A con los impares de B. 
# (valores pares o valores impares se refiere a los elementos propiamente 
# dichos y no a sus posiciones).
#· La concatenación de los valores impares de A con el reverso de  los valores pares de B. 
#· La intercalación de los elementos de A y B


#Objetivo: función que intercala los elementos de dos listas y genera una nueva
#Parámetros de entrada: dos listas
#Parámetro de salida: una nueva lista 

def intercarlarListas(listaUno, listaDos):
    lista=[]
    
    for i in range(len(listaUno)):
        lista.append(listaUno[i])
        lista.append(listaDos[i])
        
    return lista
        
    
    

#Objetivo: función que genera una nueva lista con los impares de A y el reverso de los pares de B 
#Parámetros de entrada: dos listas
#Parámetro de salida: una nueva lista 

def concatenarImparesyReverso(listaUno,listaDos):
    lista=[]
    for i in range(len(listaUno)):
        if listaUno[i]%2!=0:
            lista.append(listaUno[i])
    pares=[]
    for i in range(len(listaDos)):
        if listaDos[i]%2==0:
            pares.append(listaDos[i])
    for num in pares:
        numero_invertido = 0
        while num > 0:
            ultimo_digito = num % 10
            numero_invertido = numero_invertido * 10 + ultimo_digito
            num //= 10
        lista.append(numero_invertido)
    return lista


#Objetivo: función que generar x números aleatorios
#Parámetros de entrada: Número entero que indica la cantidad de elementos
#Parámetro de salida: Número 
def generarListaAleatoria(N):
    lista=[]
    for i in range(N):
        lista.append(random.randint(1,100))
    return lista 

#Objetivo: concatenar valores pares de primer lista con impares de segunda lista
#Parámetros de entrada: Dos listas
#Parámetro de salida: Lista 
def concatenarValoresParesEImpares(listaUno,listaDos):
    lista=[]
    
    for i in range(len(listaUno)):
        if listaUno[i]%2==0:
            lista.append(listaUno[i])
    
    for i in range(len(listaDos)):
        if listaDos[i]%2!=0:
            lista.append(listaDos[i])
    return lista
    

#Programa Principal
cantidad= int(input("Ingrese la cantidad de registros que desee que tenga la lista\n"))
A = generarListaAleatoria(cantidad)
B = generarListaAleatoria(cantidad)

print("Primer Lista",A)
print("Segunda Lista",B)

C = concatenarValoresParesEImpares(A,B)

print("Lista con pares de A e impares de B ",C)


D = concatenarImparesyReverso(A,B)

print("Lista con impares de A y el reverso de los pares de B", D)

E = intercarlarListas(A,B)

print("Lista intercalada de dos listas ",E)