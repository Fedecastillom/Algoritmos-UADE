#Escribir una función para devolver una lista con todas las posiciones 
# que ocupa  un valor pasado como parámetro, utilizando búsqueda binaria en una lista 
# ordenada. 
# La función debe devolver una lista vacía si el elemento no se encuentra en la lista original

def busquedabinaria(lista, dato):
    izq = 0
    der = len(lista) - 1
    pos_inicial = -1
    
   
    while izq <= der and pos_inicial == -1:
        centro = (izq + der) // 2
        if lista[centro] == dato:
            pos_inicial = centro
            der=centro-1
            print(pos_inicial,"imprimo julia")
        elif lista[centro] < dato:
            izq = centro + 1
        else:
            der = centro - 1
            
    if pos_inicial == -1:
        return []

    posiciones = []

    izq = pos_inicial
    while izq >= 0 and lista[izq] == dato:
        posiciones.append(izq)
        izq -= 1


    der = pos_inicial + 1
    while der < len(lista) and lista[der] == dato:
        posiciones.append(der)
        der += 1

    return posiciones
            


lista=[1,2,3,4,5,6,6,6,7,8,9,10,11]

pos=busquedabinaria(lista,6)

print(pos)