class Orden:

    contador_ordenes = 0

    def __init__(self, computadoras):
        Orden.contador_ordenes += 1

        self._id_orden = Orden.contador_ordenes
        self._computadoras = computadoras

    def agregar_computadora(self, newComputadora):
        self._computadoras.append(newComputadora)

    def __str__(self):
        computadoras_str = ''

        for computadora in self._computadoras:
            computadoras_str += computadora.__str__()
        return f'''
                    ORDEN: {self._id_orden},
                    COMPUTADORAS: {computadoras_str}
                '''