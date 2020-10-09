#Ejercicio 7: Crear un programa que calcule el sueldo bruto de una persona que trabaja de lunes a viernes 8 hs
# y su pago por hora es de 400 pesos. Devolver el sueldo por pantalla.

"""Declaro variables para ingresar por teclado cantidad de horas y días trabajados"""

horas_trabajadas = int(input('Ingrese el NUMERO de horas trabajadas por día'))
dias_trabajados = int(input('Ingrese la cantidad de días trabajados'))
valor_hora = 400

"""Declaro la variable sueldo bruto, que se compone del producto de las variables anteriores"""
sueldobruto = horas_trabajadas * dias_trabajados * valor_hora

print(f'Su sueldo bruto es de ${sueldobruto}')

