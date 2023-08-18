from LaboratorioMundoPC.Monitor import Monitor
from LaboratorioMundoPC.Raton import Raton
from LaboratorioMundoPC.Teclado import Teclado


class Computadora():

    contador_computadora = 0

    def __init__(self, nombre, monitor, teclado, raton):
        Computadora.contador_computadora += 1

        self._id_computadora = Computadora.contador_computadora
        self._nombre = nombre
        self._monitor = monitor
        self._teclado = teclado
        self._raton = raton

    def __str__(self):
        return f'''
                {self._nombre}: {self._id_computadora}
                Monitor: {self._monitor}
                Teclado: {self._teclado}
                Raton: {self._raton}
                '''

if __name__ == '__main__':
    #para crear una computadora necesito crear los demas elementos
    teclado = Teclado('DELL', 'USB')
    raton = Raton('DELL', 'Bluethoot')
    monitor = Monitor('DELL', 15)

    computadora = Computadora('DELL', monitor, teclado, raton)
    print(computadora)