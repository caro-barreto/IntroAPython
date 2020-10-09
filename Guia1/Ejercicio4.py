#Ejercicio 4: Crear un programa que pregunte al usuario su nombre y devuelva "¡Hola {nombre}!"
"""
Creo la variable nombre, cuyo valor será ingresado por teclado
"""
nombre = input('Ingrese su nombre')
""" Creo la variable saludo, que tomará el dato de nombre para saludar al usuario"""
saludo = (f'Hola {nombre}!')
"""Muestro el valor de la variable saludo por consola usando la función predeterminada print """
print(saludo)