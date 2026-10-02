import math

def pedir_nombre():
    while True:
        nombre = input("Nombre del estudiante: ").strip()
        if nombre == "":
            print("ERROR: El nombre no puede estar vacío.")
        else:
            return nombre

def pedir_calificacion(numero):
    while True:
        texto = input(f"Calificación {numero}: ").strip().replace(",", ".")
        try:
            nota = float(texto)
        except ValueError:
            print("ERROR: No se permite texto, solo números.")
            continue

        if not math.isfinite(nota):
            print("ERROR: Ingrese un número válido.")
        elif nota < 0:
            print("ERROR: La calificación tiene que ser positiva.")
        elif nota > 100:
            print("ERROR: La calificación máxima es 100.")
        else:
            return nota

nombre = pedir_nombre()
nota1 = pedir_calificacion(1)
nota2 = pedir_calificacion(2)
nota3 = pedir_calificacion(3)

promedio = (nota1 + nota2 + nota3) / 3

print("Estudiante:", nombre)
print("Promedio:", round(promedio, 2))
if promedio >= 51:
    print("Estado: APROBADO")
else:
    print("Estado: REPROBADO")