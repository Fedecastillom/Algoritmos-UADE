#Ejercicio 1: Realizar un programa para ingresar desde el teclado un conjunto de números. 
# Al  finalizar mostrar por pantalla el primer y último valor ingresado. Finalizar la lectura con -1.

print("#####EJERCICIO 1########")
numero=int(input("Ingrese un número y para finalizar ingrese -1\n"))
primer_valor=numero
ultimo_valor=numero

while numero!=-1:
    ultimo_valor=numero
    numero=int(input("Ingrese un número y para finalizar ingrese -1\n"))


if primer_valor!=-1 and ultimo_valor!=-1:
    print("El primer valor es ", primer_valor, " y el ultimo valor es ",ultimo_valor)
else:
    print("Ingreso un valor inválido")
    

print("#####EJERCICIO 2########")
#Ejercicio 2: Realizar un programa para ingresar desde el teclado un conjunto de números e  
# informar si la cantidad de elementos es impar o par, sin utilizar contadores. Finalizar la lectura de datos con -1. 

#La inicializo en False porque aún no he ingresado ningun valor
esImpar=False

numero=int(input("Ingrese un número y para finalizar presione -1\n"))

if numero!=-1:
    #Lo modifico a True porque en la linea 26 ya ingrese un valor
    esImpar=True
    while(numero!=-1):
        numero=int(input("Ingrese un número y para finalizar presione -1\n"))
        #Modifico el estado al contrario en cada iteración si el número ingresado no es -1
        if numero!=-1:
            esImpar=not esImpar
        
       

if esImpar:
    print("La cantidad de números ingresados es impar")
else:
    print("La cantidad de números ingresados es par")



print("#####EJERCICIO 3########")
#Realizar un programa para ingresar desde el teclado un conjunto de números y mostrar 
# por pantalla el menor y el mayor de ellos. Finalizar la lectura de datos  con un valor -1.

numerito=int(input("Ingrese un número\n"))

if numerito!=-1:
    mayor=numerito
    menor=numerito
    
    while numerito!=-1:
        numerito=int(input("Ingrese un número\n"))
        
        if numerito>mayor and numerito!=-1:
            mayor=numerito
        
        if numerito<menor and numerito!=-1:
            menor=numerito
        
    print("El mayor número ingresado es: ",mayor)
    print("El menor número ingresado es: ",menor)
else:
    print("Usted ingreso -1")
            


print("#####EJERCICIO 4########")
#Ejercicio 4: Desarrollar un programa que imprima la suma de los números impares comprendidos entre 42 y 176.

#Utilizo un for, coloco 173 porque la función range le resta uno al tope
suma_impares=0
for i in range(46,173):
    if i%2!=0:
        suma_impares+=i

print("La suma de los números impares entre 46 y 172 es: ",suma_impares)


print("#####EJERCICIO 5########")
#Ejercicio 5: Desarrollar un programa que imprima los números 
# naturales comprendidos entre  1 y N. El valor de N se ingresa desde el teclado.


tope= int(input("Ingrese un número tope\n"))
contador=0

if tope>0:
    while contador<=tope:
        print(contador)
        contador+=1
else:
    print("Valor inválido")
    
print("#####EJERCICIO 6########")

#Ejercicio 6: Mostrar la tabla de multiplicar (entre 1 y 12) del número 4. 
# ¿Cómo cambiaría el  algoritmo para que el usuario pueda decidir la tabla de multiplicar a mostrar?

numeroTabla= int(input("Ingrese el número del que quiere saber la tabla\n"))

for i in range(1,13):
    resultado=numeroTabla*i
    print(numeroTabla,"x ",i,"=",resultado)


print("#####EJERCICIO 7########")
#Ejercicio 7: Leer 10 números enteros e imprimir su promedio, el mayor valor leído 
# y en qué  posición se encontraba. Si se ingresó más de una vez sólo debe informar la primera.

mayor=0
suma=0
posicion=0

for i in range(1,11):
    numero=int(input("Ingrese un número\n"))
    if numero>mayor:
        posicion=i
        mayor=numero
    suma+=numero 

promedio=suma/10

print("El mayor número ingresado es ",mayor, " y se ingreso en la posición ",posicion)
print("El promedio de los números ingresados es: ",promedio)
        
print("#####EJERCICIO 8########")
#Ejercicio 8: Ingresar números, hasta que la suma de los números pares supere 100. 
# Mostrar cuántos números se ingresaron en total.

sumaPares=0
contador=0

while sumaPares<100:
    numero=int(input("Ingrese un número\n"))
    if numero%2==0:
        sumaPares+=numero
    contador+=1

print("Se ingresaron ", contador, " en total")



print("#####EJERCICIO 9########")
#Ejercicio 9: Se desea analizar cuántos autos circulan con patente con numeración 
# par y cuántos con numeración impar en un día. 
# Escribir un programa que permita ingresar la terminación de la patente (entre 0 y 9) hasta ingresar 
# -1 e informe  cuántos vehículos pasaron con numeración par y cuántos con numeración impar.

terminacion=int(input("Ingrese la terminación de su patente entre 0 y 9\n"))

if terminacion!=-1:
    cantPar=0
    cantImpar=0
    
    while terminacion!=-1:
        if terminacion>=0 and terminacion<=9:
            if terminacion%2==0:
                cantPar+=1
            else:
                cantImpar+=1
        else:
            print("Ingreso un valor inválido")
        terminacion=int(input("Ingrese la terminación de la patente\n"))
    print("La cantidad de patentes pares que ingreso son ",cantPar)
    print("La cantidad de patentes impares que ingreso son ",cantImpar)
else:
    print("No ingreso valores")
    
    
print("#####EJERCICIO 10########")

#Ejercicio 10: El factorial de un número entero N mayor que 
# cero se define como el producto  de todos los enteros X 
# tales que 0 < X <= N. 
# Desarrollar un programa para calcular el factorial de un número dado. 
# Deberán rechazarse las entradas inválidas  (menores que 0).

numeroFactorial=int(input("Ingresar el número al que le quiere sacar el factorial\n"))
factorial=1
if numeroFactorial<0:
    print("Ingreso un valro inválido")
elif numeroFactorial==0:
    factorial=1
else:
    for i in range(1,numeroFactorial+1):
        factorial*=i

print("El factorial de ", numeroFactorial, " es ", factorial)

print("#####EJERCICIO 11########")
#Ejercicio 11: Realizar un programa que lea un número 
# natural H e imprima un mensaje indicando 
# si H es primo o no. Se dice que un número es 
# primo cuando sólo es divisible por sí mismo y por la unidad.

h=int(input("Indique el valor del que quiere saber si es primo\n"))

#Los numeros menores o iguales a 1 no son primos
if h<=1:
    print("No es primo")
else:
    esPrimo=True
    for i in range(2,h):
        if h%i==0:
            esPrimo=False
    if esPrimo:
        print("El numero",h, "es primo")
    else:
        print("El numero ",h, "no es primo")

print("#####EJERCICIO 12########")
#Ejercicio 12: La sucesión de Fibonacci es una sucesión 
# de números enteros donde cada término se obtiene 
# como suma de los dos anteriores, siendo los dos primeros 0 y 1.  
# Por lo tanto, Fib=0, 1, 1, 2, 3, 5, 8, 13, 21.... 
# Realizar un programa que lea N e  imprima los N primeros 
# términos de esta sucesión, como así también la suma de  los mismos

fibo=int(input("Ingrese el valor hasta el que se quiere sacar la serie de Fibonacci\n"))

a=0
b=1

print("Los primeros ",fibo," terminos de la sucesión de Fibonacci son: ")
print(a, " ,")
if fibo>0:
    print(b," , ")

suma_fibonacci=a+b
contador=2

while contador<fibo:
    temp=a
    a=b
    b=temp+b
    
    suma_fibonacci+=b
    print(b," , ")
    contador+=1