#Ejercicio 5: Crear un programa que pida al usuario ingresar 2 números por teclado y devuelva por pantalla
# la suma de ellos en un renglón, la resta en otro, el producto en otros y la división en otro.
""" Declaramos dos variables cuyo valor será un numero (int) ingresado por el usuario"""
num1 = int(input('Ingrese un número entero'))
num2 = int(input('Ingrese un número entero'))

"""Declaramos variables que representen las operaciones que queremos realizar entre los numeros ingresados"""

suma = num1 + num2
resta = num1 - num2
producto = num1 * num2
division = float(num1/num2)

"""Utilizo la función print para mostrar por consola el resultado de las operaciones definidas anteriormente"""
print(f'El resultado de la suma entre ambos números es {suma}')
print(f'El resultado de la resta entre ambos números es {resta}')
print(f'El resultado del producto entre ambos números es {producto}')
print(f'El resultado de la división entre ambos números es {division}')
