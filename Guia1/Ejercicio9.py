#Ejercicio 9: Crear un programa que pregunte al usuario 5 números enteros y devuelva una lista con ellos.
"""Declaramos 5 variables que luego serán elementos de nuestra lista, las mismas son numeros ingresados
por teclado
"""
num1 = int(input('Ingrese un número entero'))
num2 = int(input('Ingrese un número entero'))
num3 = int(input('Ingrese un número entero'))
num4 = int(input('Ingrese un número entero'))
num5 = int(input('Ingrese un número entero'))
"""Creamos una lista que se componga de las variables ingresadas anteriormente"""
lista_numeros = [num1, num2, num3, num4, num5]
"""Mostramos la lista por consola usando la funcion predetermianda print"""
print(lista_numeros)