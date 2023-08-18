from Producto import Producto

class Orden:
    contador_ordenes = 0

    def __init__(self, productos):
        Orden.contador_ordenes += 1
        self._productos = list(productos)
        self._id_orden = Orden.contador_ordenes

    def agregar_productos(self, newProducto):
        self._productos.append(newProducto)

    def calcular_total(self):
        total = 0
        for producto in self._productos:
            total += producto.precio
        return total

    def __str__(self):
        producto_str = ''
        for producto in self._productos:
            producto_str += f' {producto.__str__()} ---'
        return f'''
                Orden: {self._id_orden},
                Productos: {producto_str}
                '''

if __name__ == '__main__':
    productoPrueba = Producto('Espejo', 100)
    print(productoPrueba)
    productoPrueba2 = Producto('Mueble', 300)
    print(productoPrueba2)

    productosList = Orden([productoPrueba, productoPrueba2])
    print(productosList)