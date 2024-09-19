print("#####Ejercicio 1\n")
#Crear el algoritmo en PSEINT para calcular sueldo de un trabajador 
#conociendo número horas trabajadas y la tarifa por hora 

horasTrabajadas= int(input("Ingrese la cantidad de horas trabajadas\n"))
tarifaHora= float(input("Ingrese la tarifa por hora\n"))

sueldo=horasTrabajadas*tarifaHora

print("El sueldo correspondiente es: ",sueldo)


print("#####Ejercicio 2\n")
#Crear un algoritmo en PSEINT para calcular la media (promedio) 
# de tres números que se deben leer.

numeroUno= int(input("Ingrese el primer número\n"))
numeroDos= int(input("Ingrese el segundo número\n"))
numeroTres=int(input("Ingrese el tercer número\n"))

promedio=(numeroUno+numeroDos+numeroTres)/3

print("El promedio de los tres números es: ",promedio)

print("#####Ejercicio 3\n")
#Crear un algoritmo en PSEINT que calcule el IVA (21%) de producto dado 
# su precio venta sin IVA. 

precioProducto=float(input("Ingrese el precio del producto\n"))
precioIVA=precioProducto*0.21

print("El precio del producto es ",precioProducto, " y el costo del IVA es ",precioIVA)

print("#####Ejercicio 4\n")
#Calcule la superficie de un rectangulo

base=float(input("Ingrese la base del rectangulo\n"))
altura=float(input("Ingrese la altura del rectangulo\n"))
superficie=base*altura
print("La superficie del rectangulo ",superficie)

print("#####Ejercicio 5\n")
#Ingresar dos números enteros A y B a través de teclado. 
#Imprimir su suma y su diferencia

a = int(input("Ingrese un número\n"))
b = int(input("Ingrese otro número\n"))

suma=a+b
resta=a-b

print("La suma de los dos números: ",suma)
print("La resta de los dos números: ", resta)

print("#####Ejercicio 6\n")
#Calcular el promedio de las notas que obtiene un alumno a partir de dos parciales

notaParcial1=float(input("Ingrese la nota del primer parcial \n"))
notaParcial2=float(input("Ingrese la nota del segundo parcial\n"))

notaFinal=(notaParcial1+notaParcial2)/2

print("La nota final del alumno es: ",notaFinal)

print("#####Ejercicio 7\n")
#Crear el algoritmo en PSEINT que permita ingresar la edad de una persona años 
# y convierta días, imprimiendo resultado. 
# Considerar todos los tienen 365 días. 

edad=int(input("Ingrese su edad\n"))
cantDias=edad*365

print("De acuerdo a su edad, usted vivio ",cantDias, " días")

print("#####Ejercicio 8\n")
#Crear un algoritmo en PSEINT que calcule el descuento
# y importe a pagar por medicamento adquirido una farmacia. 
# El precio del mismo se ingresa teclado. 
# El descuento es de 35%. 
# Se solicita informar original, monto de descuento y monto final 

precio=float(input("Ingrese el precio del producto\n"))
descuento=precio*0.35
precioConDescuento=precio-descuento

print("El precio original del producto es ",precio," y el descuento es: ",descuento, "\nEl precio final es: ",precioConDescuento)


print("#####Ejercicio 9\n")
#Crear un algoritmo en PSEINT donde tres personas ingresen 
# la cantidad de dinero que aportan para fundar una empresa, 
# y se informe el porcentaje aporto cada uno 

aporteUno = float(input("Ingrese la cantidad de dinero aportado por la primer persona\n"))
aporteDos = float(input("Ingrese la cantidad de dinero que aporto la segunda persona\n"))
aporteTres= float(input("Ingrese la cantidad de dinero que aporto la persona tres\n"))

total=aporteUno+aporteDos+aporteTres

porcUno = (aporteUno*100)/total
porcDos= (aporteDos*100)/total
porcTres= (aporteTres*100)/total

print("La primer persona aporto ",aporteUno, " por lo tanto representa ",porcUno, " %")
print("La segunda persona aporto ",aporteDos, " por lo tanto representa ",porcDos, " %")
print("La tercera persona aporto ",aporteTres, " por lo tanto representa ",porcTres, " %")

print("#####Ejercicio 10\n")
#Crear un algoritmo en PSEINT que lea medida metros e 
# imprimir esta expresada centímetros, pulgadas, pies y yardas. 
# Los factores de conversión son: 
#1 pie = 12 pulgadas
#1 yarda= 3pies 
# 1 pulgada= 2.54 
#1 metro = 100 cm 

cantMetros=float(input("Ingrese la cantidad de metros\n"))
cantCm= cantMetros*100
cantPulgadas = cantCm/2.54
cantPie= cantPulgadas/12
cantYardas=cantPie/3
print(cantMetros, " en centimetros representa ", cantCm, " centimetros")
print(cantMetros, " en pulgadas representa ", cantPulgadas, " pulgadas")
print(cantMetros, " en pies representa ", cantPie, " pies")
print(cantMetros, " en yardas representa ", cantYardas, " yardas")


print("#####Ejercicio 11\n")
#Una inmobiliaria paga a sus vendedores un salario de $250000, 
# más una comisión 50000 por cada venta realizada, más el 5% del valor las ventas. 
# Se debe imprimir número vendedor y el salario que le corresponde en determinado mes. 
# Se leen el número de vendedor, la cantidad ventas realizó total mismas y el valor
#de las mismas

nombre=input("Ingrese el nombre del vendedor:\n")
cantVentas=int(input("Ingrese la cantidad de ventas:\n"))
valorTotal= float(input("Ingrese el valor total de las ventas\n"))

salarioVendedor=250000+(50000*cantVentas)+(0.05*valorTotal)

print("El vendedor ",nombre," le corresponde un salario total de ",salarioVendedor)

print("#####Ejercicio 12\n")
#Un productor agrícola desea estimar cuántos quintales de trigo puede 
#producir en su parcela. 
#Escribir un algoritmo para ingresar el largo y ancho metros la misma determinar 
# rinde sabiendo que 10 m2 se obtienen 2 quintales. 

largo=float(input("Ingrese el largo de la parcela en metros\n"))
ancho = float(input("Ingrese el ancho de la parcela en metros\n"))

areaParcela=largo*ancho

rinde=(2/10)*areaParcela

print("El rinde estimado es: ",rinde)


print("#####Ejercicio 13\n")
#Leer un período en segundos e imprimirlo expresado días, horas, minutos y segundos. 
# Por ejemplo, 200000 equivalen a 2 días 7 horas  33 minutos y 20 segundos 
# Leer un período en segundos e imprimirlo expresado días, horas, minutos y segundos. 

cantSegundosTotales=int(input("Ingrese la cantidad de segundos\n"))

#Un dia tiene 24*3600=86400 segundos 
cantDias= cantSegundosTotales//(24*3600)
segundosSobrantes= cantSegundosTotales% (24*3600)
horas=segundosSobrantes//3600
segundosSobrantes=segundosSobrantes%3600
minutos=segundosSobrantes//60
segundosSobrantes=segundosSobrantes%60

print(f"Usted ingreso {cantSegundosTotales}\n y representan: \n {cantDias} días \n {horas} horas \n {minutos} minutos y {segundosSobrantes} segundos")



print("#####Ejercicio 14\n")
#Un banco necesita para sus cajeros automáticos un programa 
# que lea una cantidad de dinero e imprima a cuántos billetes equivale, 
# considerando existen $1000, 500, 100, 50, 10, 5 y 1. 
# Desarrollar dicho algoritmo tal forma se minimice la entregados por el cajero. 

cantDinero=int(input("Ingrese la cantidad de dinero\n"))

print(f"La cantidad total de dinero ingresado es {cantDinero}")

cantBilletes_1000 = cantDinero//1000

cantDinero%=1000

cantBilletes_500 = cantDinero//500

cantDinero%=500

cantBilletes_100= cantDinero//100
cantDinero%=100

cantBilletes_50=cantDinero//50
cantDinero%=50

cantBilletes_10=cantDinero//10
cantDinero%=10

cantBilletes_5=cantDinero//5
cantDinero%=5

cantBilletes_1=cantDinero//1

print(f"\nEl cual esta compuesto por \n -> Billetes de 1000 {cantBilletes_1000} \n -> Billetes de 500: {cantBilletes_500}\n -> Billetes de 100: {cantBilletes_100}\n -> Billetes de 50: {cantBilletes_50}\n -> Billetes de 10: {cantBilletes_10}\n -> Billetes de 5: {cantBilletes_5} \n-> Billetes de 1: {cantBilletes_1}")


