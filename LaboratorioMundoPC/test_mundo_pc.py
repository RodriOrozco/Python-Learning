from LaboratorioMundoPC.Computadora import Computadora
from LaboratorioMundoPC.Monitor import Monitor
from LaboratorioMundoPC.Raton import Raton
from LaboratorioMundoPC.Teclado import Teclado
from Orden import Orden

teclado = Teclado('DELL', 'USB')
raton = Raton('DELL', 'Bluethoot')
monitor = Monitor('DELL', 15)
computadora = Computadora('DELL', monitor, teclado, raton)

teclado2 = Teclado('Acer', 'Bluethoot')
raton2 = Raton('Acer', 'Bluethoot')
monitor2 = Monitor('Acer', 31)
computadora2 = Computadora('Acer', monitor2, teclado2, raton2)

teclado3 = Teclado('HP', 'USB')
raton3 = Raton('HP', 'USB')
monitor3 = Monitor('HP', 24)
computadora3 = Computadora('HP', monitor3, teclado3, raton3)

computadorasList = [computadora, computadora2, computadora3]
orden = Orden(computadorasList)
print(orden)
