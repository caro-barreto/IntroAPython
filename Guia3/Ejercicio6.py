#Ejercicio 6: Crear una función que devuelva por pantalla un mensaje ingresado por parámetro pero en modo Title.
# Si el mensaje ya está en modo title, que devuelva por pantalla "El mensaje ya está en modo title: {mensaje}"

def metodo_title(mensaje):
    if mensaje.istitle():
        print(f'El mensaje ya está en modo title: {mensaje}')
    else:
        print(mensaje.title())

mensaje = input('Ingrese su mensaje')
metodo_title(mensaje)
