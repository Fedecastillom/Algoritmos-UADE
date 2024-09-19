def busquedabinaria(lista, dato):
    izq = 0
    der = len(lista) - 1
    pos = -1
    
    while izq <= der and pos == -1:
        centro = (izq + der) // 2
        if lista[centro] == dato:
            pos = centro
        elif lista[centro] < dato:
            izq = centro + 1
        else:
            der = centro - 1
            
    return pos


lista=[1,2,3,4,5,6,7,8,9,10,11]

pos=busquedabinaria(lista,6)

print(pos)