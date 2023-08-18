class Producto:

    contador_productos = 0

    def __init__(self, nombre, precio):
        Producto.contador_productos += 1
        self._nombre = nombre
        self._precio = precio
        self._id_producto = Producto.contador_productos

    def __str__(self):
        return f'''
                ID: {self._id_producto}
                Producto: {self._nombre}
                Precio: {self._precio}
                '''
    #-----------GETTERS------------
    @property
    def precio(self):
        return self._precio

if __name__ == '__main__':
    productoPrueba = Producto('Espejo', 100)
    print(productoPrueba)
    productoPrueba2 = Producto('Mueble', 300)
    print(productoPrueba2)

