#Ejercicio 3: Crear una función que, a partir de un mensaje, nos devuelva una lista con todos los números, si los hay,
# que aparecen en dicho mensaje.


mensaje = input('Ingrese un mensaje: ')

def buscador_numeros(mensaje):
    lista_numeros = []
    for i in mensaje:
        if i.isdigit():
            lista_numeros.append(i)
    print(lista_numeros)

buscador_numeros(mensaje)
