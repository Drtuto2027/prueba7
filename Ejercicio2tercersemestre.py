class Estudiante():
    def __init__(self, nombre, edad, sexo, nota):
        self.nombre = nombre
        self.edad = edad
        self.sexo = sexo.lower()
        self.nota = nota
    def getNombre(self):
        return self.nombre
    def getEdad(self):
        return self.edad
    def getSexo(self):
        return self.sexo
    def getNota(self):
        return self.nota
    def setNombre(self, nombre):
        self.nombre = nombre
    def setEdad(self, edad):
        self.edad = edad
    def setSexo(self, sexo):
        self.sexo = sexo.lower()
    def setNota(self, nota):
        self.nota = nota

    def calcularAprobados(self, estudiantes):
        hombresAprobados = 0
        mujeresAprobadas = 0
        for i in estudiantes:
            if i.getNota() >= 4.5 and i.getSexo() == 'f':
                mujeresAprobadas += 1
            elif i.getNota() >= 4.5 and i.getSexo() == 'm':
                hombresAprobados += 1
        print(f'La cantidad de mujeres aprobadas es: {mujeresAprobadas}')
        print(f'La cantidad de hombres aprobados es: {hombresAprobados}')
    
    def nombresAprobados(self, estudiantes):
        aprobados = []
        for i in estudiantes:
            if i.getNota() >= 4.5:
                aprobados.append(i.getNombre())
        print(f'Los nombres de los estudiantes aprobados son: {aprobados}')