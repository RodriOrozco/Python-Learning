class Persona:
    def __init__(self, nombre, edad):
        self._nombre = nombre
        self._edad = edad

    def __add__(self, other):
        return f'{self._nombre} {other._nombre}'

    def __sub__(self, other):
        return self._edad - other._edad

persona1 = Persona('Juan', 50)
persona2 = Persona('Carlos', 30)

print(persona1 + persona2)
print(persona1 - persona2)
