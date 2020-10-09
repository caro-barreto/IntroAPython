#Ejercicio 10: Utilizar el método range() para recorrer el iterable e imprimir solo los números impartes entre 1 y 40 inclusive.

#numeros = list(range(0,41))

for numero in range(0, 41):
    if numero % 2 != 0:
        print(numero)
        