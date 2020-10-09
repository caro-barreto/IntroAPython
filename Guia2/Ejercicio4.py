#Ejercicio 4: Ingresar 6 números por teclado, preferentemente enteros, ordenarlos de manera creciente e imprimirlos por pantalla.
lista_numeros = []

for i in range (6):
    numero = int(input('Ingrese un numero'))
    lista_numeros.append(numero)

lista_numeros.sort()

for numero in lista_numeros:
    print(numero)

