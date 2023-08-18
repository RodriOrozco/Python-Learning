from DispositivoEntrada import DispositivoEntrada

class Raton(DispositivoEntrada):

    contador_ratones = 0

    def __init__(self, marca, tipo_entrada, ):
        Raton.contador_ratones += 1
        self._id_raton = Raton.contador_ratones

        super().__init__(marca, tipo_entrada)

    def __str__(self):
        return f'ID: {self._id_raton}, MARCA: {self._marca}, TIPO: {self._tipo_entrada}'

