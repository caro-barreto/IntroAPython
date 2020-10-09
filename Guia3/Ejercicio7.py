#Ejercicio 7: Crear una función que verifique si una palabra es un palíndromo o no. En caso de que lo sea devolver
# por pantalla "La palabra es un palíndromo", en caso contrario, devolver "La palabra no es un palíndromo".

def es_palindromo(palabra):
    palabra_al_reves = palabra[::-1]
    if palabra == palabra_al_reves:
        print(f'La palabra {palabra} es un palíndromo')
    else:
        print(f'La palabra {palabra} no es un palíndromo')

word = input('Ingrese una palabra para analizar si es o no un palíndromo')
es_palindromo(word)
