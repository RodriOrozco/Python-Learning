class FiguraGeometrica:
    def __init__(self, ancho, alto):
        #validaciones para los datos proporcionados
        if 0 < ancho < 20:
            self._ancho = ancho
        else:
            self._ancho = 0

        if 0 < alto < 20:
            self._alto = alto
        else:
            self._alto = 0

    def _validar_valor(self, valor):
        return True if 0 < valor < 20 else False

class Color:
    def __init__(self, color):
        self._color = color