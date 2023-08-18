class Vehiculo:
    def __init__(self, color, ruedas):
        self._color = color
        self._ruedas = ruedas

    def __str__(self):
        return f'color: {self._color}, ruedas: {self._ruedas}'

class Bicicleta(Vehiculo):
    def __init__(self, color, ruedas, tipo):
        super().__init__(color, ruedas)
        self._tipo = tipo

    def __str__(self):
        return f'{super().__str__()}, tipo: {self._tipo}'

class Coche(Vehiculo):
    def __init__(self, color, ruedas, velocidad):
        super().__init__(color, ruedas)
        self._tipo = velocidad

    def __str__(self):
        return f'{super().__str__()}, velocidad: {str(self._ruedas)}'