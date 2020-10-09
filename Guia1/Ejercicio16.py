#Ejercicio 16: Crear un programa que cree un diccionario vacío y lo vaya llenado con información sobre una persona
# (por ejemplo nombre, edad, sexo, teléfono, correo electrónico, etc.) que se le pida al usuario. Cada vez que se añada un nuevo dato
# debe imprimirse el contenido del diccionario.
"""creo diccionario vacio"""
datos_personales = {

}
continuar = 'si'
"""Declaro una variable continuar, que usaré para saber si el usuario desea agregar mas información o terminar el bucle
si el valor coincide con el de la variable el bucle se repite, si no el bucle termina"""

while continuar == 'si':
    key = input('¿Qué dato desea guardar en el diccionario?')
    value = input(f'{key} : ')
    datos_personales[key] = value
    print(datos_personales)
    continuar = input('Desea agregar más información? ingrese si para continuar')

"""Siempre que continuar sea igual a si, el programa pedirá la clave y luego el valor por input y los guardará en el diccionario"""

