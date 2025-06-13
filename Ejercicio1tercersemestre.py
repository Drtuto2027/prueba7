class Producto():
    def __init__(self,nombre,categoria,precioNeto,precioTotal,iva):
        self.nombre = nombre
        self.categoria = categoria.lower()
        self.precioNeto = precioNeto
        self.precioTotal = precioTotal
        self.iva = iva

    #metodos consultores y modificadores
    def getNombre(self):
        return self.nombre
    def getCategoria(self):
        return self.categoria
    def getPrecioNeto(self):
        return self.precioNeto
    def getPrecioTotal(self):
        return self.precioTotal
    def getIva(self):
        return self.iva
    
    def setNombre(self,nombre):
        self.nombre = nombre
    def setCategoria(self,categoria):
        self.categoria = categoria.lower()
    def setPrecioNeto(self,precioNeto):
        self.precioNeto = precioNeto
    def setPrecioTotal(self,precioTotal):
        self.precioTotal = precioTotal
    def setIva(self,iva):
        self.iva = iva

    #funciones
    def calcularAcumuladoGranos(self,Productos):
        acumulado = 0
        categoria = 'granos'
        for i in Productos:
            if i.categoria == categoria:
                acumulado = acumulado + i.precioTotal
        print('el valor total de los productos de categoria granos es de: ',acumulado)

    def calcularAcumuladoLacteos(self,Productos):
        acumulado = 0
        categoria = 'lacteos'
        for i in Productos:
            if i.getCategoria() == categoria and i.getPrecioNeto() > 13000:
                acumulado = acumulado + i.getPrecioNeto()
        print('el valor total de los productos de categoria lacteos es de: ',acumulado)

    def calcularPromedioVerduras(self,Productos):
        acumulado = 0
        promedio = 0
        cantidad = []
        categoria = 'verduras'
        for i in Productos:
            if i.getCategoria() == categoria:
                acumulado += i.getPrecioNeto()
                cantidad.append(i)
        if cantidad == 0:
            print('no hay productos de categoria verduras')
        else:
            promedio = acumulado / len(cantidad)
            print('el promedio de los productos de categoria verduras es de: ',promedio)

    def calcularPromedioAseo(self,Productos):
        acumulado = 0
        promedio = 0
        cantidad = []
        categoria = 'aseo'
        for i in Productos:
            if i.getCategoria() == categoria and i.getPrecioTotal() < 20000:
                acumulado += i.getPrecioTotal()
                cantidad.append(i)
        if len(cantidad) == 0:
            print('no hay productos de categoria aseo con un precio total menor a 20000')
        else:
            promedio = acumulado / len(cantidad)
            print('el promedio de los productos de categoria aseo es de: ',promedio)
        promedio = acumulado / len(cantidad)