from Empleado import Empleado
from Gerente import Gerente

def imprimir_detalles(objeto):
    print(type(objeto))
    print(objeto.mostrar_detalle())
    if isinstance(objeto, Gerente):
        print(objeto._departamento)


empleado = Empleado('Martin', 3000)
imprimir_detalles(empleado)

gerente = Gerente('Ramiro', 5000, 'tecnologia')
imprimir_detalles(gerente)