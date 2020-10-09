#Ejercicio 8: Crear una función que calcule cuántos litros de nafta gasta un auto que consume 2 litros x 100km,
# en un viaje ida y vuelta MdP-Bue si la distancia es de 400km. Luego crear una función que, a partir de esos datos,
# devuelva cuánto significa eso en pesos si el litro de nafta está 60$.

def consumo_nafta():
    kms_por_litro = 50
    kms_viaje = int(input('Ingrese la cantidad de kms de viaje a realizar'))
    total_litros = kms_viaje / kms_por_litro
    return total_litros
cantidad_litros = consumo_nafta()

def costo_nafta(litros):
    costo_litro = 60
    costo_total = cantidad_litros * costo_litro
    print(f'El costo total del viaje es de ${costo_total}')
costo_nafta(cantidad_litros)

