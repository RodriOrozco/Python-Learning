class Empleado:
    def __init__(self, nombre, sueldo):
        self._nombre = nombre
        self._sueldo = sueldo

    def __str__(self):
        return f'Nombre: {self._nombre}, sueldo: {self._sueldo}'

    def mostrar_detalle(self):
        return self.__str__()

