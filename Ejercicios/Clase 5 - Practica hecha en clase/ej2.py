#Ejercicio 2: Escribir un programa que permita ingresar los números 
# de legajo de los alumnos  de un curso y su nota de examen final. 
# El fin de la carga se determina ingresando un -1 en el legajo. 
# Informar para cada alumno si aprobó o no el examen considerando que se aprueba con nota mayor 
# o igual a 4. Se debe validar que la  nota ingresada sea entre 1 y 10. Terminada la carga de datos, informar:
#Cantidad de alumnos que aprobaron con nota mayor o igual a 4.
#Cantidad de alumnos que desaprobaron el examen con nota menor a 4.
#Porcentaje de alumnos que están aplazados (tienen 1 en el examen).

aprobados = 0
desaprobados = 0
aplazados = 0
total_alumnos = 0

bandera=True
while bandera:
    legajo  = int(input("Ingrese el número de legajo del alumno (o -1 para finalizar): "))
    
    if legajo == -1:
        bandera=False
    else:
        nota  = float(input(f"Ingrese la nota de examen para el alumno {legajo}: "))
        if nota>=1 and nota <= 10:
            total_alumnos += 1
            if nota >= 4:
                print(f"El alumno {legajo} aprobó el examen.")
                aprobados += 1
            elif nota<4 and nota>1:
                print(f"El alumno {legajo} desaprobó el examen.")
                desaprobados += 1
            elif nota==1:
                print(f"El alumno {legajo} aplazo el examen.")
                aplazados += 1
        else:
            print("Error: Por favor, ingrese una nota válida (entre 1 y 10)")

if total_alumnos != 0:
    porcentaje_aplazados = (aplazados / total_alumnos) * 100
    print("Resultados:")
    print("Cantidad de alumnos que aprobaron con nota mayor o igual a 4:", aprobados)
    print("Cantidad de alumnos que desaprobaron el examen con nota menor a 4:", desaprobados)
    print("Porcentaje de alumnos que están aplazados (tienen 1 en el examen):", porcentaje_aplazados, "%")
else:
    print("No ingreso alumnos")


