#Ejercicio 6: Crear un programa que calcule cuánto dinero tendré al cabo de un mes si deposito
# hoy 2000 en el banco y el interés mensual es de 5%, y luego devuelva por pantalla ese valor.

"""Declaro una variable con la cantidad de dinero que tengo"""

dinero_inicial = 2000 #Podria ingresarse por teclado tmb y serviría para otras cantidades

"""Al multiplicarlo por un numero, devuelve ese numero + 5%"""
interes_mensual = 1.05

"""El dinero inicial multiplicado por el interés ganado da como resultado lo que se tiene al cabo de un mes"""
dinero_final = dinero_inicial * interes_mensual

"""Muestro el resultado por consola usando la función print"""

print(f'El total al cabo de un mes es de ${dinero_final}')
