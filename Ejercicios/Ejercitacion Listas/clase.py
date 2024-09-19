
#7) Encontrar el segundo mayor número en una lista 

def informarMaximo(lista):
        max=lista[0]
        for i in range(len(lista)):
            if lista[i]>max:
                max=lista[i]
        return max

def encontrarSegundoMayor(lista):
    if len(lista)<2:
        return -1 
    else:
        max=informarMaximo(lista)
        segundoMaximo=None
        for i in range(len(lista)):
            if (segundoMaximo==None and lista[i]!=max) or (lista[i]<max and lista[i]>segundoMaximo):   
                segundoMaximo=lista[i]
       
        return segundoMaximo

print(encontrarSegundoMayor([15,15,9,5,6,14,8,7,16,23]))
