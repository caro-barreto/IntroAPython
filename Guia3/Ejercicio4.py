#Ejercicio 4: Crear una función que, a partir de 4 números, devuelva el mayor producto de dos de ellos. Imprimir resultado por pantalla.

def producto_mayores():
    numeros = []
    for i in range(4):
        n = int(input('Ingrese un numero: '))
        numeros.append(n)
    numeros.sort()
    a = numeros[-1]
    b = numeros[-2]
    resultado = a * b
    print(resultado)
producto_mayores()

