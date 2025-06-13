class Estudiante():
    def __init__(self, nombre, edad, sexo, nota):
        self.nombre = nombre  # Inicializa el nombre del estudiante
        self.edad = edad  # Inicializa la edad del estudiante
        self.sexo = sexo.lower()  # Inicializa el sexo del estudiante y lo convierte a minúsculas
        self.nota = nota  # Inicializa la nota del estudiante
    
    # Métodos para obtener los valores de los atributos
    def getNombre(self):
        return self.nombre

    def getEdad(self):
        return self.edad

    def getSexo(self):
        return self.sexo

    def getNota(self):
        return self.nota
    
    # Métodos para establecer nuevos valores en los atributos
    def setNombre(self, nombre):
        self.nombre = nombre

    def setEdad(self, edad):
        self.edad = edad

    def setSexo(self, sexo):
        self.sexo = sexo.lower()

    def setNota(self, nota):
        self.nota = nota
    
    # Método para calcular la cantidad de estudiantes aprobados según el sexo
    def calcularAprobados(self, estudiantes):
        hombresAprobados = 0
        mujeresAprobadas = 0
        for i in estudiantes:
            if i.getNota() >= 4.5 and i.getSexo() == 'f':  # Verifica si la nota es mayor o igual a 4.5 y si el sexo es femenino
                mujeresAprobadas += 1
            elif i.getNota() >= 4.5 and i.getSexo() == 'm':  # Verifica si la nota es mayor o igual a 4.5 y si el sexo es masculino
                hombresAprobados += 1
        print(f'La cantidad de mujeres aprobadas es: {mujeresAprobadas}')
        print(f'La cantidad de hombres aprobados es: {hombresAprobados}')
    
    # Método para obtener los nombres de los estudiantes aprobados
    def nombresAprobados(self, estudiantes):
        aprobados = []
        for i in estudiantes:
            if i.getNota() >= 4.5:  # Verifica si la nota es mayor o igual a 4.5
                aprobados.append(i.getNombre())
        print(f'Los nombres de los estudiantes aprobados son: {aprobados}')
