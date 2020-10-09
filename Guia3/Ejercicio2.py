#Ejercicio 2: Crear una función que devuelva una lista con todos los números pares del 0 al 100 inclusive.
# Imprimir esa lista por pantalla.

lista_pares = []
def pares():
    for n in range (101):
        if n % 2 == 0:
            lista_pares.append(n)
    print(lista_pares)
pares()
