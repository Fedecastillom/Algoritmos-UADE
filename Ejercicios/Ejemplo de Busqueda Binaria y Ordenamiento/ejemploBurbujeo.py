def metodoIntercambio(lista):
    desordenada=True
    while desordenada:
        desordenada=False
        for i in range(len(lista)-1):
            if lista[i]>lista[i+1]:
                aux=lista[i]
                lista[i]=lista[i+1]
                lista[i+1]=aux
                desordenada=True
    return lista

lista=[87,65,43,134,1,24,325]
metodoIntercambio(lista)
print(lista)
