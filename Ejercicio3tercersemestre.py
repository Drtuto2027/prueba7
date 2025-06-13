class Votante():
    def __init__(self, nombre, edad, sexo):
        self.nombre = nombre
        self.edad = edad
        self.sexo = sexo.lower()

    def getNombre(self):
        return self.nombre
    def getEdad(self):
        return self.edad 
    def getSexo(self):
        return self.sexo
    def setNombre(self, nombre):
        self.nombre = nombre
    def setEdad(self, edad):
        self.edad = edad
    def setSexo(self, sexo):
        self.sexo = sexo.lower()

    
    def edad18y20(self,votantes):
        cantidad = 0
        for i in votantes:
            if i.getEdad() >=18 and i.getEdad() <=20:
                cantidad += 1
        print('la cantidad de votantes entre 18 y 20 años es: ',cantidad)
    
    def edad20y30(self,votantes):
        cantidad = 0
        for i in votantes:
            if i.getEdad() >20 and i.getEdad() <=30:
                cantidad += 1
        print('la cantidad de votantes entre 20 y 30 años es: ',cantidad)
    
    def edad30(self,votantes):
        cantidad = 0
        for i in votantes:
            if i.getEdad() > 30:
                cantidad += 1
        print('la cantidad de votantes mayores a 30 años es: ',cantidad)