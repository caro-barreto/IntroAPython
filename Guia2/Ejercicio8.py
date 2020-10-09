#Ejercicio 8: Pedirle al usuario que ingrese por teclado 3 números binarios de 8 bits, para cada uno imprimir su siguiente
# (número + 1) pero en sistema decimal. Recuerden que los números binarios están compuestos por 1 y 0.


#Dejo al input como string para poder usar int() en la conversión.

for i in range(3):
    binario = input('Ingrese un numero binario de 8 bits')
    decimal = int(binario, 2)  #int() para convertir en entero, 2 es la base de los binarios.
    siguiente = decimal + 1
    print(siguiente)