#Eliminar de una lista de números enteros los valores que se encuentren en una 
#segunda lista. Imprimir la lista original, la lista de valores a eliminar y la lista 
#resultante. Ambas listas deben rellenarse con números al azar. La cantidad y el 
#rango de los valores los decide el programador
import random
def generarListaAleatoria(N):
    lista=[]
    while len(lista)<N:
        numero= random.randint(0,100)
        if numero==0:
            bandera=False
        else:
            lista.append(numero)
    return lista 


def eliminarValores(listaOriginal,elementosEliminar):
    i=0
    while i<len(elementosEliminar):
        j=0
        while j<len(listaOriginal):
            if elementosEliminar[i]==listaOriginal[j]:
                del listaOriginal[j]
            j+=1
        i+=1
    
    return listaOriginal 
        

#Programa Principal 

cant=int(input("Ingrese la cantidad de elementos que desee que tenga su lista\n"))

listaOriginal=generarListaAleatoria(cant)
listaEliminar=generarListaAleatoria(cant)

print("Lista original", listaOriginal)
print("Elmentos a eliminar: ",listaEliminar)
print("Lista con eliminados: ",eliminarValores(listaOriginal,listaEliminar))