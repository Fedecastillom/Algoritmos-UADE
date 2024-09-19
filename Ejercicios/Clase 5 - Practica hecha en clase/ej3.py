#Ejercicio 3: Una empresa aplica el siguiente procedimiento en la comercialización de sus productos:
#Aplica el precio base a la primera docena de unidades.
#Aplica un 10% de descuento a todas las unidades entre 13 y 100.
#Aplica un 25% de descuento a todas las unidades por encima de las 100.
#Por ejemplo, supongamos que vende 230 unidades de un producto cuyo precio  base es 100. 
# El cálculo resultante 
# sería: 100 * 12 + 90 * 88 + 75 * 130 = 18870 y el precio promedio es de 18870/230 = 82.04
#Escribir un programa que lea la cantidad solicitada de un producto y su precio  base, 
# y muestre el valor total de la venta y el precio promedio por unidad. 
# El fin  de carga se determina ingresando -1 como cantidad solicitada. Al finalizar informar: 
#Cantidad de ventas realizadas total.
#Cantidad de ventas en las que se aplicó un 10% de descuento.
#Cantidad de ventas en las que SOLO se aplicó el precio base, es decir  que no se le realizaron descuentos.

ventas_totales = 0
descuento_10_porcentaje = 0
precio_base_solo = 0
bandera=True
precio_promedio=0

while bandera:
    cantidad = int(input("Ingrese la cantidad solicitada del producto (o -1 para finalizar): "))
    
    if cantidad == -1:
        bandera=False
    else:
        precio_base=float(input("Ingrese el precio base del producto: "))
        if cantidad <= 12:
            valor_total = cantidad * precio_base
            precio_base_solo += 1
            precio_promedio=valor_total/cantidad
        elif cantidad>=13 and cantidad <= 100:
            valor_total = 12 * precio_base + (cantidad - 12) * (precio_base * 0.9)
            descuento_10_porcentaje += 1
            precio_promedio=valor_total/cantidad
        else:
            valor_total = 12 * precio_base + 88 * (precio_base * 0.9) + (cantidad - 100) * (precio_base * 0.75)
            descuento_10_porcentaje += 1
            precio_promedio=valor_total/cantidad
        ventas_totales += 1
    
print("El valor total de las ventas realizadas es:", valor_total)
print("Precio promedio por unidad:", precio_promedio)
print("Cantidad de ventas realizadas total:", ventas_totales)
print("Cantidad de ventas en las que se aplicó un 10% de descuento:", descuento_10_porcentaje)
print("Cantidad de ventas en las que SOLO se aplicó el precio base:", precio_base_solo)
