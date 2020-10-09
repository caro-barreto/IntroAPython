#Ejercicio 3: Pedir al usuario que ingrese por teclado 2 números, si el primero es menor que el segundo imprimir la resta entre
#el segundo y el primero, si el primero es mayor que el segundo imprimir la suma de ambos, y si son iguales imprimir su producto.

num1 = int(input('Ingrese un número'))
num2 = int(input('Ingrese un número'))

if num1 < num2:
    resta = num2 - num1
    print(f'El resultado de la resta entre el segundo numero menos el primero es {resta}')
elif num1 > num2:
    suma = num1 + num2
    print(f'La suma entre ambos numeros es {suma}')
else:
    producto = num1 * num2
    print(f'El producto entre ambos números es {producto}')