#Ejercicio 10: Escribir un programa que almacene todas las letras del abecedario y luego elimine las vocales
# y nos devuelva una lista sin las vocales, sin modificar la original.

abecedario1 = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'ñ', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

abecedario_sin_vocales = abecedario1.copy()

for i in abecedario_sin_vocales:
    vocales = ['a', 'e', 'i', 'o', 'u']
    for vocal in vocales:
        if i == vocal:
            abecedario_sin_vocales.remove(i)

print(abecedario_sin_vocales)

#este me costó, lei del manual sobre métodos pero tuve que mirar la solución porque estaba haciendo lio con el for

