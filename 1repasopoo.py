class Votante:
    def __init__(self, nombre, edad, sexo):
        self.nombre = nombre
        self.edad = edad
        self.sexo = sexo

# Función para cargar votantes en una lista
def cargar_votantes():
    lista_votantes = []
    for i in range(18):
        nombre = input(f'Nombre del votante {i+1}: ')
        edad = int(input(f'Edad del votante {i+1}: '))
        sexo = input(f'Sexo del votante {i+1} (M/F): ')
        votante = Votante(nombre, edad, sexo)
        lista_votantes.append(votante)
    return lista_votantes

# Función para contar votantes por rangos de edad
def contar_votantes(lista_votantes):
    rango_18_20 = 0
    rango_21_30 = 0
    mayor_30 = 0

    for votante in lista_votantes:
        if 18 <= votante.edad <= 20:
            rango_18_20 += 1
        elif 21 <= votante.edad <= 30:
            rango_21_30 += 1
        elif votante.edad > 30:
            mayor_30 += 1

    return rango_18_20, rango_21_30, mayor_30

# Cargar la lista de votantes
lista_votantes = cargar_votantes()

# Contar votantes por rangos de edad
rango_18_20, rango_21_30, mayor_30 = contar_votantes(lista_votantes)

# Resultados
print(f"\nVotantes con edad entre 18 y 20 años: {rango_18_20}")
print(f"Votantes con edad entre 21 y 30 años: {rango_21_30}")
print(f"Votantes con edad mayor a 30 años: {mayor_30}")
