#ABS = Abstract Base Class
from abc import ABC, abstractmethod

class FiguraGeometrica(ABC):
    def __init__(self, alto, ancho):
        if validar_valor(alto):
            self._alto = alto
        else:
            print('El alto proporcionado debe ser entre 0 a 20')
        if validar_valor(ancho):
            self._ancho = ancho
        else:
            print('El ancho proporcionado debe ser entre 0 a 20')
    #-------GETTERS------------
    @property
    def alto(self):
        return self._alto
    @property
    def ancho(self):
        return self._ancho
    #------SETTERS-------------
    @alto.setter
    def alto(self, newAlto):
        if validar_valor(newAlto):
            self._alto = newAlto
        else:
            self._alto = 0
            print('El alto proporcionado debe ser entre 0 a 20')
    @ancho.setter
    def ancho(self, newAncho):
        if validar_valor(newAncho):
            self._ancho = newAncho
        else:
            self._ancho = 0
            print('El ancho proporcionado debe ser entre 0 a 20')
    #-------METODOS------------
    @abstractmethod #esto obliga a las clases hijas a implementar los metodos, sino se transforman en clases abstractas y no pueden ejecutarse
    def calcular_area(self):
        pass


class Color:
    def __init__(self, color):
        self._color = color


class Cuadrado(FiguraGeometrica, Color):
    def __init__(self, lado, color):
        FiguraGeometrica.__init__(self, lado, lado)
        Color.__init__(self, color)

    def calcular_area(self):
        return self.alto * self.ancho

#-------validaciones---------
def validar_valor(value):
    return True if 0 < value < 20 else False

#-------instancias----------
cuadrado1 = Cuadrado(5, 'rojo')
print(cuadrado1.calcular_area())