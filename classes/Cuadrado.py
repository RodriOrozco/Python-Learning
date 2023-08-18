from ClaseExtendida import FiguraGeometrica
from ClaseExtendida import Color

class Cuadrado(FiguraGeometrica, Color):
    #le pasa solo lado, para luego pasarle a la clase padre el mismo lado tanto a ancho y alto
    def __init__(self, lado, color):
        #se respeta el llamado segun el orden de los parametros para la extension
        FiguraGeometrica.__init__(self, lado, lado)
        Color.__init__(self, color)

    def calcular_area(self):
        #aca utiliza el valor de lado, que a su vez lo recibe por parametros la clase Padre, pero se llama a los atributos de la clase padre
        return f'Calculo del area: {int(self._ancho) * int(self._alto)}'

cuadrado1 = Cuadrado(10, 'rojo')
print(cuadrado1.calcular_area())

#MRO - Method Resolution Object
print(Cuadrado.mro())
#rta: [<class '__main__.Cuadrado'>, <class 'ClaseExtendida.FiguraGeometrica'>, <class 'ClaseExtendida.Color'>, <class 'object'>]
#Es importante el orden de la extension de las clases

