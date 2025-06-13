class Producto():
    def __init__(self, nombre, categoria, precioNeto, precioTotal, iva):
        self.nombre = nombre
        self.categoria = categoria.lower()
        self.precioNeto = precioNeto
        self.precioTotal = precioTotal
        self.iva = iva

    # Métodos consultores
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
    
    # Métodos modificadores
    def setNombre(self, nombre):
        self.nombre = nombre

    def setCategoria(self, categoria):
        self.categoria = categoria.lower()

    def setPrecioNeto(self, precioNeto):
        self.precioNeto = precioNeto

    def setPrecioTotal(self, precioTotal):
        self.precioTotal = precioTotal

    def setIva(self, iva):
        self.iva = iva

    # Funciones para calcular acumulados y promedios
    def calcularAcumuladoGranos(self, Productos):
        acumulado = 0
        categoria = 'granos'
        for i in Productos:
            if i.categoria == categoria:
                acumulado += i.precioTotal
        print('El valor total de los productos de categoría granos es de: ', acumulado)

    def calcularAcumuladoLacteos(self, Productos):
        acumulado = 0
        categoria = 'lacteos'
        for i in Productos:
            if i.getCategoria() == categoria and i.getPrecioNeto() > 13000:
                acumulado += i.getPrecioNeto()
        print('El valor total de los productos de categoría lácteos es de: ', acumulado)

    def calcularPromedioVerduras(self, Productos):
        acumulado = 0
        cantidad = 0
        categoria = 'verduras'
        for i in Productos:
            if i.getCategoria() == categoria:
                acumulado += i.getPrecioNeto()
                cantidad += 1
        if cantidad == 0:
            print('No hay productos de categoría verduras')
        else:
            promedio = acumulado / cantidad
            print('El promedio de los productos de categoría verduras es de: ', promedio)

    def calcularPromedioAseo(self, Productos):
        acumulado = 0
        cantidad = 0
        categoria = 'aseo'
        for i in Productos:
            if i.getCategoria() == categoria and i.getPrecioTotal() < 20000:
                acumulado += i.getPrecioTotal()
                cantidad += 1
        if cantidad == 0:
            print('No hay productos de categoría aseo con un precio total menor a 20000')
        else:
            promedio = acumulado / cantidad
            print('El promedio de los productos de categoría aseo es de: ', promedio)
