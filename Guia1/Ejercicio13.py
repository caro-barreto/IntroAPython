#Ejercicio 13: Crear un programa que guarde en una variable el diccionario {'Euro':'€', 'Dollar':'$', 'Yen':'¥'},
# pregunte al usuario por una divisa y muestre su símbolo o un mensaje de aviso si la divisa no está en el diccionario

diccionario_divisas = {
    'Euro':'€',
    'Dollar':'$',
    'Yen':'¥'
}
consulta_divisas = input('Ingrese el nombre de una divisa para conocer su símbolo')

if consulta_divisas in diccionario_divisas:
    print(diccionario_divisas[consulta_divisas])
else:
    print('La divisa no está en el diccionario')