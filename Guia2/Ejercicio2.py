#Ejercicio 2: Crear una lista con 10 números enteros cualquiera. Indicar cuál es el número mayor y cuál es el número menor.
# Si al menos hay 3 números mayores a 100, imprimir esos números, si no, imprimir los números menores a 50 que formen parte de la lista.

lista_numeros = [23, 6, 98, 56, 4, 123, 567, 875, 334, 23]
lista_numeros.sort()

print(f'El mayor número es {lista_numeros[-1]}')
print(f'El menor número es {lista_numeros[0]}')

mayores100 = []

for numero in lista_numeros:
    if numero > 100:
        mayores100.append(numero)

if len(mayores100) >= 3:
    for numero in mayores100:
        print(numero)
else:
    for numero in lista_numeros:
        if numero < 50:
            print(numero)