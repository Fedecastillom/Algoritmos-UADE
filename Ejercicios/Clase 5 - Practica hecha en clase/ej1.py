#Ejercicio 1: Leer números que representan edades de un grupo de personas, 
# finalizando la  lectura cuando se ingrese el número -1. Imprimir cuántos 
# son menores de 18  años, cuántos tienen 18 años o más y el promedio de edad de ambos grupos. 
# Descartar valores que no representan una edad válida. (Se considera válida una  edad entre 0 y 100).


bandera=True
sumaMenor18=0
sumaMayor18=0
cantMayor18=0
cantMenor18=0


while bandera:
    edad=int(input("Ingrese la edad de la persona\n"))
    if edad==-1:
        bandera=False
    else: 
        if edad<0 or edad>100:
            print("Ingreso una edad invalida")
        elif edad<18:
                cantMenor18+=1
                sumaMenor18+=edad
        else:
                cantMayor18+=1
                sumaMayor18+=18

if cantMayor18!=0: 
    promediomayor18=sumaMayor18/cantMayor18
    print("El promedio de la cantidad de edades mayores a 18 son ",promediomayor18)
    print("La cantidad de registros mayores de 18 son ", cantMayor18)
else:
    print("No ingreso personas mayores de 18")

if cantMenor18!=0:
    promediomenor18= sumaMenor18/cantMenor18
    print("El promedio de la cantidad de edades menores a 18 son ",promediomenor18)
    print("La cantidad de registros menores a 18 son ", cantMenor18)
else:
    print("No ingreso personas menores de 18")


