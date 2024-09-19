#Ejercicio 1: Escribir una función que reciba como parámetros dos números enteros. 
# Calcular  y devolver el resultado de la multiplicación de ambos valores 
# utilizando solamente sumas. 
# Por ejemplo 4 * 3 = 4 + 4 + 4 .

def multiplicacion_por_sumas(num1,num2):
    resultado=0
    while num2>0:
        resultado+=num1
        num2-=1
    return resultado

#Ejercicio 2: Dados dos parámetros enteros A y B, obtener AB 
# (A elevado a la B) mediante  multiplicaciones sucesivas, 
# utilizando la función del ejercicio anterior para multiplicar. 
# Por ejemplo 43 = 4 * 4 * 4.

#Otra opción para este ejercicio es desde esta función llamar a la anterior

def exponencial_por_sumas(base,exponente):
    resultado=1
    while exponente>0:
        resultado*=base
        exponente-=1
    return resultado

#Ejercicio 3: Imprimir una columna de asteriscos, donde su altura se recibe como parámetro.

def imprimir_piramide_astericos(altura):
    contador=0
    while contador<altura:
        print("*")
        contador+=1

#Ejercicio 4: Devolver True si el número entero recibido como primer parámetro 
# es múltiplo del segundo, o False en caso contrario. 
# Ejemplo: esmultiplo(40, 8) devuelve True  y esmultiplo(50, 3) devuelve False.

def esmultiplo(a,b):
    if a%b==0:
        return True
    else:
        return False


#Ejercicio 5: Desarrollar la función signo(n), que reciba un número entero 
# y devuelva 1, -1 o  0 según el valor recibido sea positivo, negativo o nulo.

def informar_signo(numero):
    if numero>0:
        return 1
    elif numero<0:
        return -1
    else:
        return 0

#Ejercicio 6: Escribir la función comparar(a, b) que reciba como parámetros dos números enteros 
# y devuelva 1 si el primero es mayor que el segundo, 0 si son iguales o -1 si  el primero 
# es menor que el segundo. 
# En este ejercicio debe aprovecharse la función del ejercicio anterior. 
# Ejemplo: comparar(4, 2) devuelve 1, y comparar(2, 4)  devuelve -1.

def comparar(a,b):
    resta=a-b
    resultado= informar_signo(resta)
    return resultado

#Ejercicio 7: Calcular y devolver el Máximo Común Divisor de dos enteros no negativos, 
# basándose en las siguientes fórmulas matemáticas:
#MCD(X,X) = X
#MCD(X,Y) = MCD(Y, X)
#Si X > Y => MCD(X, Y) = MCD(X-Y, Y).
#Ejemplo: MCD(40, 15) devuelve 5

#MCD= Si son iguales es ese numero
#MCD: es el numero entero mas grande que divide exactamente (sin decimales) a los dos numeros

def mcd(numero1,numero2):
    if numero1<0 or numero2<0:
        print("No se puede calcular el Maximo comun denominador de numeros negativos")
    #Sin son iguales, ese es el MCD
    else:
        while numero2!=0:
            aux=numero2
            numero2=numero1%numero2
            numero1=aux 
        return numero1
                    
    

#Ejercicio 8: La raíz cuadrada de un número positivo n puede calcularse mediante 
# la siguiente  fórmula de Newton:
#donde a es una aproximación a n. 
# Al aplicar repetidamente esta fórmula reemplazando a por 
# la aproximación obtenida en el paso anterior, se obtiene cada vez  
# una aproximación mejor. Desarrollar un programa que calcule la raíz cuadrada  
# aproximada de un número entero positivo n utilizando como primera aproximación a n/2.
# Detener el proceso cuando la diferencia entre dos cálculos sucesivos  sea menor a 0,0001.

def raiz_cuadrada_newton(numero):
    primerAprox=numero/2
    diferencia = 1 #Cualquier valor para que el while ingrese
    corte = 0.0001
 
    while diferencia > corte:
        nueva_aproximacion = ((numero/primerAprox)+primerAprox) / 2
        diferencia = primerAprox - nueva_aproximacion
        primerAprox = nueva_aproximacion
    return primerAprox


#Ejercicio 9: Escribir una función que reciba como parámetros un número de día, un número  de mes 
# y un número de año y devuelva la cantidad de días que faltan hasta fin  de mes. 
# Luego desarrollar tres programas para: 
#Ingresar una fecha formada por tres enteros (día, mes y año) 
# e imprimir  la cantidad de días que faltan hasta fin de año.
#Ingresar una fecha formada por tres enteros (día, mes y año) 
# e imprimir la cantidad de días transcurridos en ese año hasta esa fecha.
#Ingresar dos fechas formadas por tres enteros (día, mes y año) 
# e imprimir cuánto tiempo transcurrió entre ambas, expresando el resultado en  años, meses y días.
#Los tres programas deben realizar su trabajo a través de la función indicada al  comienzo.

def calcular_dias_hasta_fin_mes(dia,mes,anio):
    bisiesto=False
    if anio%400==0 or (anio%4==0 and anio%100!=0):
        bisiesto=True
    if dia<0 or dia>31:
        return -1
    elif mes==1 or mes==3 or mes==5 or mes==7 or mes==8 or mes==10 or mes==12:
        return 31-dia
    elif mes==2 and bisiesto:
        return 29-dia
    elif mes==2 and not bisiesto:
        return 28-dia
    elif mes==4 or mes==6 or mes==9 or mes==11:
        return 30-dia
    else:
        return -1

def calcular_dias_fin_anio(dia,mes,anio):
    diasFaltantes=calcular_dias_hasta_fin_mes(dia,mes,anio)
    iterador=mes+1
    dia=0
    
    while iterador<=12:
        diasFaltantes+=calcular_dias_hasta_fin_mes(dia,iterador,anio)
        iterador+=1
    return diasFaltantes

def calcular_dias_hasta_hoy(dia,mes,anio):
    diasTranscurrido=dia
    iterador=mes-1
    dia=0
    while iterador>=1:
        diasTranscurrido+=calcular_dias_hasta_fin_mes(dia,iterador,anio)
        iterador-=1
    return diasTranscurrido


def diferenciaEntreFechas(dia1,mes1,anio1,dia2,mes2,anio2):
    dias_transcurridos_fecha_fin= calcular_dias_hasta_hoy(dia2,mes2,anio2)
    dias_transcurridos_fecha_inicio=calcular_dias_hasta_hoy(dia1,mes1,anio1)
    
    dias_diferencia=dias_transcurridos_fecha_fin-dias_transcurridos_fecha_inicio
    
    anios=dias_diferencia//365
    dias_restantes=dias_diferencia%365
    meses= dias_restantes//30
    dias=dias_restantes%30
    return anios, meses,dias 
    

#Ejercicio 10: Extraer un dígito de un número. 
# La función recibe como parámetros dos números  enteros, 
# uno será del que se extraiga el dígito y el otro indica qué cifra se desea  obtener. 
# La cifra de la derecha se considera la número 0. 
# Retornar el valor -1 si  no existe el dígito solicitado. 
# Tener en cuenta que el número puede ser positivo o  negativo. 
# Ejemplo: extraerdigito(12345, 1) devuelve 4, y extraerdigito(12345, 8) devuelve -1.

def extraerDigito(numero, posicion):
    if numero<0:
        numero*=-1
    contador=0
    
    while numero>0:
        
        ultNumero=numero%10
        
        if contador==posicion:
            return ultNumero

        numero=numero//10
        contador+=1
    return -1
    

#Ejercicio 11: Obtener el dígito central de un número entero pasado como parámetro, 
# sólo si la  cantidad de dígitos es impar. Si la longitud fuera par devolver -1. Ejemplo: 
#digitocentral(12345) devuelve 3, y digitocentral(123456) devuelve -1.

def extraerDigitoCentral(num):
    aux=num 
    if num<0:
        num*=-1
    
    cantDigitos=0
    
    while num>0:
        num=num//10
        cantDigitos+=1
        
    if cantDigitos%2==0:
        return -1
    else:
        mediana=cantDigitos//2
        return extraerDigito(aux,mediana)
    

#Programa Principal 

#Invocación para Ejercicio 1

print("Ejercicio 1")
numero1 = int(input("Ingrese el primer numero de la multiplicación\n"))
numero2= int(input("Ingrese el segundo número de la multiplicación\n"))

print("El resultado de la multplicación es: ", multiplicacion_por_sumas(numero1,numero2))


#Invocación a la función del ejercicio 2

print("Ejercicio 2")

base=int(input("Ingrese la base para la potencia\n"))
exponente= int(input("Ingrese el numero exponente\n"))

print("El resultado de ",base," elevado a ",exponente, " es ",exponencial_por_sumas(base,exponente))



#Invocación a la función del ejercicio 3

print("Ejercicio 3")
altura= int(input("Ingrese la altura de la columna de asteriscos que desea imprimir\n"))
imprimir_piramide_astericos(altura)

#Invocación a la función del ejercicio 4

print("Ejercicio 4")

x = int(input("Ingrese el primer número para luego determinar si el segundo es módulo de este\n"))
y = int(input("Ingrese el segundo número para determinar si el primero es modulo de este\n"))

print(x," es modulo de ",y," ? ",esmultiplo(x,y))

#Invocación a la función del ejercicio 5
print("Ejercicio 5")
numerito = int(input("Ingrese un número para determinar el signo\n"))

signo = informar_signo(numerito)

if signo==0:
    print("No tiene signo")
elif signo==1:
    print("Es positivo")
else:
    print("Es negativo")
    

#Invocación a la función del ejercicio 6
print("Ejercicio 6")
primerNumero=int(input("Ingrese el primer numero\n"))
segundoNumero= int(input("Ingrese el segundo número\n"))

resultado=comparar(primerNumero,segundoNumero)

if resultado==1:
    print("El primero es mayor que el segundo")
elif resultado==-1:
    print("El segundo es mayor")
else:
    print("Son iguales")
    
#Invocación a la función del ejercicio 7

print("Ejercicio 7")
p= int(input("Ingrese el primer numero\n"))
q= int(input("Ingrese el segundo numero\n"))
print("El maximo comun denominador entre ",p," y ",q, " es ",mcd(p,q))

#Invocación a la función del ejercicio 8
print("Ejercicio 8")
numeroRaiz=int(input("Ingrese el número del que se quiere obtener la raiz\n"))

print("El resultado de la raiz de ",numeroRaiz," es ",raiz_cuadrada_newton(numeroRaiz))

#Invocación a la función del ejercicio 9

print("Ejercicio 9")

dia= int(input("Ingrese el numero de dia\n"))
mes= int(input("Ingrese el numero de mes\n"))
anio = int(input("Ingrese el año\n"))

print("La cantidad de dias que faltan para fin de mes es: ", calcular_dias_hasta_fin_mes(dia,mes,anio))
print("La cantidad de dias que faltan para fin de año son: ",calcular_dias_fin_anio(dia,mes,anio))
print("La cantidad de dias que transcurrieron hasta hoy son: ", calcular_dias_hasta_hoy(dia,mes,anio))

dia_hasta=int(input("Ingrese dia hasta\n"))
mes_hasta=int(input("Ingrese dia hasta\n"))
anio_hasta=int(input("Ingrese dia hasta\n"))

dif_anio, dif_mes, dif_dia = diferenciaEntreFechas(dia,mes,anio,dia_hasta,mes_hasta,anio_hasta)

print("La cantidad de dias que transcurrieron entre la primer fecha y la segunda es: ", dif_anio, " años ", dif_mes, " meses ",dif_dia, " dias " )



#Invocación función del ejercicio 10

print("Ejercicio 10")

num = int(input("Ingrese el número al que luego le desea extraer un digito\n"))
digito= int(input("Ingrese el digito que desea extraer\n"))

print("El numer que se encuentra en esa posicion es: ",extraerDigito(num,digito))


#Invocación función del ejercicio 11

print("Ejercicio 11")
numeroCentral= int(input("Ingrese el número al que le desea extraer el valor central\n"))

print("El valor que se encuentra en el centro es: ", extraerDigitoCentral(numeroCentral))