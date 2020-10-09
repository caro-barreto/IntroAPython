#Ejercicio 9: Pedirle al usuario que ingrese el monto disponible en su tarjeta de crédito. Evaluar si puede realizar una compra de $2500,
# si puede indicar cuánto saldo le queda luego de efectuarla. Si no puede, indicar cuánto dinero le falta para poder realizarla.

disponible = int(input('Ingrese el monto disponible en su tarjeta de crédito'))

if disponible >=2500:
    saldo = disponible - 2500
    print(f'Después de realizar la compra aún le queda un saldo de ${saldo}')
else:
    resto = 2500 - disponible
    print(f'Le faltan ${resto} de disponible para poder realizar la compra')