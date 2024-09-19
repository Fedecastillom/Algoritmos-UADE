
# Ejercicio 1: Ingresar dos números enteros e indicar si son iguales o distintos.

numeroUno = int(input("Ingrese el primer numero\n"))
numeroDos = int(input("Ingrese el segundo numero\n"))

if numeroUno==numeroDos:
    print("Son iguales")
else:
    print("Son distintos")


# Ejercicio 2: Leer un número entero e imprimir un mensaje indicando si es par o impar

numero =int(input("Ingresar un número\n"))

if numero%2==0:
    print("Es par")
else:
    print("Es impar")

# Ejercicio 3: Desarrollar un programa que solicite un número de mes (por ejemplo 4) y 
# escriba el nombre del mes en letras ("abril"). Verificar que el mes sea válido y 
# mostrar un mensaje de error en caso de que no lo sea.

mes = int(input("Ingrese el mes en número\n"))

if mes<1 or mes>12 :
    print("Mes inválido")
elif mes==1:
    print("Enero")
elif mes==2:
    print("Febrero")
elif mes==3:
    print("Marzo")
elif mes==4:
    print("Abril")
elif mes==5:
    print("Mayo")
elif mes==6:
    print("Junio")
elif mes==7:
    print("Julio")
elif mes==8:
    print("Agosto")
elif mes==9:
    print("Septiembre")
elif mes==10:
    print("Octubre")
elif mes==11:
    print("Noviembre")
elif mes==12:
    print("Diciembre")

# Ejercicio 4: En el congreso se vota una ley muy importante. 
# Desarrollar un programa que permita ingresar la cantidad 
# de votos a favor y en contra, e informe el porcentaje obtenido en 
# cada caso y si la misma fue aprobada o no.

votosAfavor = int(input("Ingrese la cantidad de votos a favor\n"))
votosEnContra=int(input("Ingrese la cantidad de votos en contra\n"))


porcFavor=(votosAfavor*100)/(votosAfavor+votosEnContra)
porcEnContra=(votosEnContra*100)/(votosAfavor+votosEnContra)

print("El porcentaje a favor de la ley es: ",porcFavor)
print("El porcentaje en contra de la ley es: ",porcEnContra)

if votosAfavor>votosEnContra:
    print("La ley fue aprobada")
elif votosEnContra>votosAfavor:
    print("La ley no fue aprobada")
else:
    print("Empate")    
    
# Ejercicio 5: Ingresar las notas de los dos parciales de un alumno e indicar si promocionó, 
# aprobó o si debe recuperar. Informar un error si el valor de alguna nota no está  entre 0 y 10.
# · Se promociona cuando las notas de ambos parciales son mayores o  iguales a 7.
# · Se aprueba cuando las notas de ambos parciales son mayores o iguales  a 4.
# · Se debe recuperar cuando al menos una de las dos notas es menor a 4.


notaUno = float(input("Ingrese la nota del primer parcial\n"))
notaDos = float(input("Ingrese la nota del segundo parcial\n"))

if notaUno<0 or notaUno>10 or notaDos<0 or notaDos>10:
    print("Nota inválida")
elif notaUno>=7 and notaDos>=7:
    print("Usted promociono la materia")
elif notaUno>=4 and notaDos>=4:
    print("Usted aprobo la materia")
elif notaUno<4 or notaDos<4:
    print("Usted debe recuperar la materia")

# Ejercicio 6: Una editorial determina el precio de un libro según la cantidad de páginas que contiene. 
# El costo básico del libro es de $5000, más $32 por página con encuadernación rústica. 
# Si el número de páginas supera las 300 la encuadernación  debe ser en tela, lo que incrementa el costo en $1200. 
# Además, si el número de  páginas sobrepasa las 600 se hace necesario un procedimiento 
# especial de encuadernación que incrementa el costo en otros $3360. Desarrollar un programa 
# que calcule el costo de un libro dado el número de páginas.

costoBasico=5000
encuadernacionRustica=32
cantPaginas= int(input("Ingrese la cantidad de páginas del libro\n"))
costo=0

if(cantPaginas<0):
    print("Cantidad de páginas inválidas")
elif cantPaginas<=300:
    costo=costoBasico+(32*cantPaginas)
elif cantPaginas<=600:
    costo=costoBasico+(32*cantPaginas)+1200
else:
    costo=costoBasico+(32*cantPaginas)+3360

print("El costo de impresión del libro es ",costo)


# Ejercicio 7: Un fletero requiere un programa que calcule el precio de sus viajes a partir de la 
# cantidad de kilómetros que recorre. Para eso cuenta con la siguiente tarifa:
#    · Viaje mínimo $2700. Sólo se cobra cuando el importe por kilómetro no  alcanza este mínimo.
#   · Si recorre entre 0 y 10 km: $400 por km
#   · Si recorre 10 km o más: $200 por km

cantKM = int(input("Ingrese la cantidad de kilometros recorridos:\n"))

VIAJEMINIMO=2700
costo=0
if cantKM<0:
    print("Cantidad de kilometros incorrecto")
elif cantKM>0 and cantKM<=10:
    costo=cantKM*400
else:
    costo=cantKM*200

if costo<VIAJEMINIMO:
    costo=VIAJEMINIMO


print("El costo del viaje es: ",costo)

# Ejercicio 8: Leer un número correspondiente a un año e imprimir un mensaje indicando si es bisiesto o no. 
# Un año es bisiesto cuando es divisible por 4. 
# Sin embargo, aquellos  años que sean divisibles por 4 y 
# también por 100 no son bisiestos, a menos que  también sean divisibles por 400. 
# Por ejemplo, 1900 no fue bisiesto pero sí el  2000.

anio = int(input("Ingrese el año a evaluar:\n"))

if (anio%4==0 and anio%100!=0)  or (anio%400==0):
    print("Es bisiesto")
else:
    print("No es bisiesto")

# Ejercicio 9: Leer tres números correspondientes al día, mes y año de una fecha e imprimir 
# un mensaje indicando si la fecha es válida o no.

dia=int(input("Ingrese el dia a evaluar\n"))
mes= int(input("Ingrese el mes a evaluar\n"))
anio=int(input("Ingrese el año a evaluar\n"))

if dia<1 or dia>31 or mes<1 or mes>12 or anio<0:
    print("Fecha inválida")
elif (mes==4 or mes==6 or mes==9 or mes==11) and dia>30:
    print("Fecha inválida")
elif ((anio%4==0 and anio%100!=0)  or (anio%400==0)) and dia>29 and mes==2:
    print("Fecha inválida")
elif mes==2 and dia>28 and (not((anio%4==0 and anio%100!=0)  or (anio%400==0))):
    print("Fecha inválida")
else:
    print("Fecha válida")

# Ejercicio 10: Diseñar un programa que calcule y muestre el sueldo neto de un empleado en base a su sueldo básico 
# y su antigüedad en años. 
# Si es soltero se le incrementa el sueldo en 5% del salario bruto por cada año de antigüedad, 
# mientras que si es  casado se le incrementa el sueldo en 7% del bruto por cada año de antigüedad. 
# También se le realizan los siguientes descuentos: 
# Jubilación: 11%, Obra Social:  3%, Sindicato: 3%
# Como datos de entrada se ingresa por teclado el sueldo básico, antigüedad y  
# estado civil (1 si es soltero o 2 si es casado). 
# Se debe informar: Estado Civil, Sueldo básico, Antiguedad, 
# Jubilación, Obra Social, Sindicato, Sueldo Neto

sueldoBasico= float(input("Ingrese su sueldo basico\n"))
antiguedad= int(input("Ingrese su antiguedad\n"))
estadoCivil=int(input("Ingrese 1 si es soltero, 2 si es casado\n"))
sueldoNeto=0

if estadoCivil==1:
    sueldoNeto=(sueldoBasico*0.05)*antiguedad
    estadoCivil="Soltero"
elif estadoCivil==2:
    sueldoNeto=(sueldoBasico*0.07)*antiguedad
    estadoCivil="Casado"

jubilacion= sueldoBasico*0.11
obraSocial= sueldoBasico*0.03
sindicato= sueldoBasico*0.03

sueldoNeto=sueldoBasico-jubilacion-obraSocial-sindicato+sueldoNeto

print("\t->Estado Civil: ", estadoCivil,"\n")
print("\t->Sueldo Basico: ", sueldoBasico,"\n")
print("\t->Antiguedad: ", antiguedad,"\n")
print("\t->Jubilación: ", jubilacion,"\n")
print("\t->Obra Social: ", obraSocial,"\n")
print("\t->Sindicato: ", sindicato,"\n")
print("\t->El sueldo neto resultante es: ", sueldoNeto,"\n")


