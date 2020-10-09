#Ejercicio 11: Crear una lista con varios números, luego ordenarlos de manera creciente y devolver por pantalla
# la lista ordenada y cuál es el menor y cuál el mayor.

lista_numeros = [5, 67, 89, 2334, 46, 6, 864, 322, 123, 8, 98]

"""Método sort ordena de menor a mayor siempre que sean del mismo tipo"""
lista_numeros.sort()

print(lista_numeros)
"""[-1] siempre va a devolver el último elemento, que al estar ordenados será el mayor"""
mayor = lista_numeros[-1]
"""[0] siempre devuelve el primer elemento, que al estar ordenados será el menor"""
menor = lista_numeros[0]
print(f'El menor número de la lista es {menor}')
print(f'El mayor número de la lista es {mayor}')

