def metodoInsercion(lista):
    for i in range(1,len(lista)): #Comienza en el 2do elemento
        aux =lista[i]
        j=i
        while j>0 and lista[j-1]>aux:
            lista[j]=lista[j-1]
            j=j-1
        lista[j]=aux
    return lista
        

lista=[98,335,3,5,324,35,1]

print(metodoInsercion(lista))