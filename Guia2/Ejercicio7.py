#Ejercicio 7: Crear un diccionario con 5 estudiantes y sus respectivas notas. Imprimir por pantalla los alumnos que aprobaron
# y su nota (no en forma de diccionario, si no con nombre : nota). Tener en cuenta que para aprobar el alumno debe sacarse
# una nota mayor o igual a 7 y menor o igual a 10.

notas_estudiantes = {
    'David Bowie': 8,
    'Billy Corgan':6,
    'John Frusciante': 9,
    'Steven Morrissey': 5,
    'Brian Molko': 7,
    }
for estudiante, calificacion in notas_estudiantes.items():
    if 10 >= calificacion >= 7:
        print(f'{estudiante}: {calificacion}')
