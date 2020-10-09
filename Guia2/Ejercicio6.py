#Ejercicio 6: Escribir un programa que seleccione una operación de cuatro operaciones numéricas disponibles, una vez seleccionada
# la operación, introducir dos números y ejecutar la operación.

n1 = int(input('Ingrese el primer numero'))
n2 = int(input('Ingrese el segundo numero'))

operacion = int(input('Ingrese 1 para realizar la suma, '
                  '2 para la resta, 3 para el producto, '
                  '4 para la division'))

if operacion == 1:
    print(n1 + n2)
elif operacion == 2:
    print(n1 - n2)
elif operacion == 3:
    print(n1 * n2)
elif operacion == 4:
    print(n1/n2)
else:
    print('Ingreso no válido')