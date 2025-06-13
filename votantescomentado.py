class Votante():
    def __init__(self, nombre, edad, sexo):
        self.nombre = nombre  # Inicializa el nombre del votante
        self.edad = edad  # Inicializa la edad del votante
        self.sexo = sexo.lower()  # Inicializa el sexo del votante y lo convierte a minúsculas

    # Métodos para obtener los valores de los atributos
    def getNombre(self):
        return self.nombre

    def getEdad(self):
        return self.edad

    def getSexo(self):
        return self.sexo

    # Métodos para establecer nuevos valores en los atributos
    def setNombre(self, nombre):
        self.nombre = nombre

    def setEdad(self, edad):
        self.edad = edad

    def setSexo(self, sexo):
        self.sexo = sexo.lower()

    # Método para contar la cantidad de votantes entre 18 y 20 años
    def edad18y20(self,votantes):
        cantidad = 0
        for i in votantes:
            if i.getEdad() >= 18 and i.getEdad() <= 20:  # Verifica si la edad está entre 18 y 20 años
                cantidad += 1
        print('La cantidad de votantes entre 18 y 20 años es: ', cantidad)
    
    # Método para contar la cantidad de votantes entre 20 y 30 años
    def edad20y30(self,votantes):
        cantidad = 0
        for i in votantes:
            if i.getEdad() > 20 and i.getEdad() <= 30:  # Verifica si la edad está entre 21 y 30 años
                cantidad += 1
        print('La cantidad de votantes entre 20 y 30 años es: ', cantidad)
    
    # Método para contar la cantidad de votantes mayores de 30 años
    def edad30(self,votantes):
        cantidad = 0
        for i in votantes:
            if i.getEdad() > 30:  # Verifica si la edad es mayor a 30 años
                cantidad += 1
        print('La cantidad de votantes mayores a 30 años es: ', cantidad)
