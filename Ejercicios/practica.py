#Ejercicio 1
#Escribir una función para ingresar desde el teclado una serie de números entre A 
#y B y guardarlos en una lista. En caso de ingresar un valor fuera de rango la 
# función mostrará un mensaje de error y solicitará un nuevo número. Para finalizar la 
#carga se deberá ingresar -1. La función recibe como parámetros los valores de A 
#y B, y devuelve la lista cargada (o vacía, si el usuario no ingresó nada) como 
#valor de retorno. Tener en cuenta que A puede ser mayor, menor o igual a B.


def ingresarNumeros(min,max):
    numeros=[]    
    if min>max:
        aux=min
        min=max
        max=aux
    elif min==max:
        return numeros

    bandera=True
    
    while bandera:
        numero=int(input("Ingrese un número\n"))
    
        if numero==-1:
            bandera=False 
        elif numero<min or numero>max:
            print("Error, valor invalido")
        else:
            numeros.append(numero)
    return numeros 


#Ejercicio 2: Calcular la suma de los números de la lista.
def calcularSuma(lista):
    suma=0
    
    for i in range(len(lista)):
        suma+=lista[i]
    return suma

#Ejercicio 3: Determinar si la lista es capicúa (palíndromo). Una lista capicúa se lee de igual 
#modo de izquierda a derecha y de derecha a izquierda. Por ejemplo, [2, 7, 7, 2] 
#es capicúa, mientras que [2, 7, 5, 2] no lo es.

def esCapicua(lista):
    listaInversa=[]
    
    i= len(lista)-1
    
    while i>=0:
        listaInversa.append(lista[i])
        i-=1
    print(lista)
    print(listaInversa)
    
    for i in range(len(lista)):
        if(lista[i]!=listaInversa[i]):
            return False
    
    return True 
        


#Ejercicio 4: Escribir una función para contar cuántas veces aparece un valor dentro de la 
#lista. La función recibe como parámetros la lista y el valor a buscar, y devuelve 
#un número entero.

def contarValorBuscado(lista,valor):
    cant=0
    for i in range(len(lista)):
        if lista[i]==valor:
            cant+=1
    return cant

#Desarrollar una función que reciba la lista como parámetro y devuelva una nueva 
#lista con los mismos elementos de la primera, pero en orden inverso. Por 
#ejemplo, si la función recibe [5, 7, 1] debe devolver [1, 7, 5]

def invertirLista(lista):
    listaInversa=[]
    
    i= len(lista)-1
    
    while i>=0:
        listaInversa.append(lista[i])
        i-=1
    return listaInversa
    
#Programa principal

print("Ejercicio 1")

minimo=int(input("Ingrese el minimo\n"))
maximo=int(input("Ingrese el maximo\n"))

lista=ingresarNumeros(minimo,maximo)

print("Ejercicio 2")
print(calcularSuma(lista))

print("Ejercicio 3")
print(esCapicua([1,2,2,1]))

print("Ejercicio 4")

print(contarValorBuscado(lista,5))


print("Ejercicio 5")
print(invertirLista([1,2,3,4]))