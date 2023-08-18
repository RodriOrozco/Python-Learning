from DispositivoEntrada import DispositivoEntrada

class Teclado(DispositivoEntrada):

    contador_teclado = 0

    def __init__(self, marca, tipo_entrada, ):
        Teclado.contador_teclado += 1
        self._id_teclado = Teclado.contador_teclado

        super().__init__(marca, tipo_entrada)

    def __str__(self):
        return f'ID: {self._id_teclado}, MARCA: {self._marca}, TIPO: {self._tipo_entrada}'

