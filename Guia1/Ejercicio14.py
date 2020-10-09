#Ejercicio 14: Crear un programa que pregunte al usuario su nombre, edad, dirección y teléfono y lo guarde en
# un diccionario. Después debe mostrar por pantalla el mensaje.

diccionario_datos = {
    'nombre': '',
    'edad': '',
    'direccion': '',
    'telefono': '',

}
nombre = input('Ingrese su nombre')
edad = int(input('Ingrese su edad'))
direccion = input('Ingrese su dirección')
telefono = int(input('Ingrese su teléfono'))

diccionario_datos['nombre'] = nombre
diccionario_datos['edad'] = edad
diccionario_datos['direccion'] = direccion
diccionario_datos['telefono'] = telefono

print(diccionario_datos)

