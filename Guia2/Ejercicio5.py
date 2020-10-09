#Ejercicio 5: Crear un diccionario con los meses del año de la forma { 1: "enero"}. Desafío: lograr cambiar las claves.
# Pista: si imprimen ítems del diccionario les crea una lista. Una vez que lo logren, imprimir el diccionario modificado.

diccionario_meses = {
    1: 'enero',
    2: 'febrero',
    3: 'marzo',
    4: 'abril',
    5: 'mayo',
    6: 'junio',
    7: 'julio',
    8: 'agosto',
    9: 'septiembre',
    10: 'octubre',
    11: 'noviembre',
    12: 'diciembre'
}
listado_meses = list(diccionario_meses.values()) #creo lista de valores
listado_numeros = list(diccionario_meses.keys()) #creo lista de claves

diccionario_meses.clear() #limpia el diccionario y lo deja vacio

"""Crea un nuevo diccionario con dict, y zip junta esas dos listas y hace que cada valor de la primera lista se 
corresponde con uno en la segunda.
"""
diccionario_meses = dict(zip(listado_meses, listado_numeros))
print(diccionario_meses)



