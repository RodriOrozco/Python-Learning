class Monitor():

    contador_monitor = 0

    def __init__(self, marca, tamaño ):
        Monitor.contador_monitor += 1

        self._id_raton = Monitor.contador_monitor
        self._marca = marca
        self._tamaño = tamaño

    def __str__(self):
        return f'ID: {self._id_raton}, MARCA: {self._marca}, TAMAÑO: {self._tamaño}'

