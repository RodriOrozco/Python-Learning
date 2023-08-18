from Empleado import Empleado

class Gerente(Empleado):
    def __init__(self, nombre, sueldo, departamento):
        super().__init__(nombre, sueldo)
        self._departamento = departamento

    def __str__(self):
        return f'{super().__str__()}, Departamento: {self._departamento}'