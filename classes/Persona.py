#SECCION 10 - herencia
class Persona:
    def __init__(self, nombre, apellido):
        self._nombre = nombre
        self._apellido = apellido

    def __str__(self):
        return f' Persona: {self._nombre} {self._apellido} '

    @property
    def nombre(self):
        return self._nombre
    @property
    def apellido(self):
        return self._apellido

    @nombre.setter
    def nombre(self, newNombre):
        self._nombre = newNombre
        return newNombre
    @apellido.setter
    def apellido(self, newApellido):
        self._nombre = newApellido
        return newApellido

#herencia simple
class Empleado(Persona):
    def __init__(self, nombre, apellido, sueldo):
        super().__init__(nombre, apellido)
        self._sueldo = sueldo

    def __str__(self):
        return f'{super().__str__()} {self._sueldo}'

    @property
    def sueldo(self):
        return self._sueldo

    @sueldo.setter
    def sueldo(self, newSueldo):
        self._sueldo = newSueldo
        return newSueldo
