"""Una escuela recibe un subsidio del Estado Nacional según la cantidad de alumnos que
estudien en ella.
Por cada alumno de nivel inicial recibe mensualmente $800, por cada alumno de nivel
primario recibe $1200, mientras que por cada alumno de nivel medio recibe $2100.
Elaborar un programa para leer las edades de los alumnos que concurren a la escuela,
finalizando la lectura cuando se ingrese un 0 (cero) como edad. (5 ptos)
Luego se pide: Imprimir un informe que muestre para cada nivel de enseñanza, el monto
total y la cantidad de alumnos. 
Teniendo en cuenta que:

Desde 1 hasta 5 es nivel inicial con un subsidio de $800
Desde 6 hasta 12 es nivel primario con un subsidio de $1200
Desde 13 hasta 17 es nivel secundario con un subsidio de $2100"""

def solucion():
    escuela = {
        "inicial": {"alumnos": 0, "subsidio": 800},
        "primario": {"alumnos": 0, "subsidio": 1200},
        "secundario": {"alumnos": 0, "subsidio": 210}
    }

    while True:
        edad = int(input("Ingrese la edad del alumno (0 para finalizar): "))
        if edad == 0:
            break
        
        elif 1 <= edad <= 5:
            escuela["inicial"]["alumnos"] += 1
        
        elif 6 <= edad <= 12:
            escuela["primario"]["alumnos"] += 1
        
        elif 13 <= edad <= 17:
            escuela["secundario"]["alumnos"] += 1

        else:
            print("Edad no válida")
    
    for nivel, datos in escuela.items():
        cantidad_alumnos = datos["alumnos"]
        subsidio_total = cantidad_alumnos * datos["subsidio"]
        print(f"Nivel {nivel}:")
        print(f"  Cantidad de alumnos: {cantidad_alumnos}")
        print(f"  Subsidio total: ${subsidio_total}")