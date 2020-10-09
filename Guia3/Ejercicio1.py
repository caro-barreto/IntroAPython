# Ejercicio 1: Crear una función que, a partir de un dato de entrada que sea en horas, nos informe cuántos minutos y cuántos
# segundos serían esas horas. Imprimir por pantalla dichos valores.

horas = int(input('Ingrese el número de horas'))

def conversor(horas):
    minutos = horas * 60
    segundos = horas * 3600
    print(f'{horas} horas representan {minutos} minutos o {segundos} segundos')


conversor(horas)



