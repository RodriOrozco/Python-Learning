# #SECCION 1 - tarea 1
# print('Mi primer log con Python, Hola Mundo!')
#
# #SECCION 2 - Variables
# primeraVariable = 'hola mundo!'
# print(primeraVariable) #'hola mundo!'
# print(primeraVariable) #'hola mundo!'
#
# primeraVariable = 23
# print(primeraVariable) # 23
#
# x = 10
# print(x)
# y = 13
# print(y)
# z = x + y
# print(z)
# print('Posicion de memoria de z (23) -->', id(z))
#
# #SECCION 3 - Tipos de datos
#
# numVar = 16
# print('Esto va a imprimir el tipo de dato ->', type(numVar)) # int (python esta orientado a POO, por lo que los tipos son clases)
#
# #concatenacion
# miGrupoFavorito = 'Artic Monkeys'
# print('Mi grupo favorito es:' + miGrupoFavorito)
# print('Mi grupo favorito es:', miGrupoFavorito) #Esto imprime lo mismo que arriba, la diferencia es el espacio " "
#
# num2 = '2'
# num3 = '3'
# print('concatena str ->', num2 + num3) # 23 porque es string
# print('concatena int ->', int(num2) + int(num3)) # 5 porque el string es transformado a number

#bool
# varBool = False
# print('esto imprime el bool =', varBool)
#
# questionVar = 3 > 2
# print('QuestionVar es una variable que contiene una sentencia/pregunta y responde con bool: ', questionVar)
#
# if varBool:
#     print('Se imprime si el resultado es TRUE')
# else:
#     print('Se imprime si el resultado es FALSE')

#funcion input para procesar entradas de User
# resultado = input('Escribi un mensaje bro: ')
# print('El usuario escribio: ', resultado) #Lo que se escriba por consola en este caso al correr el programa
# print("Ya finalizo la interaccion, I'll be back")
#
# primerNumero = int(input('Escribe el primer numero: '))# si se le manda un str tira error,
# segundoNumero = int(input('Escribe el segundo numero: '))# el handling error se vera mas adelante en el curso.
# sumaDeLosNumerosInput = primerNumero + segundoNumero
# print('transformamos str a int para que la entrada se pueda sumar en vez de concatenar: ', sumaDeLosNumerosInput)

#SECCION 4 - OPERADORES
"""
sumNum1 = 10
sumNum2 = 13
print(f'El resultado de la suma es: {sumNum1 + sumNum2}')#f y {} sirve para la interpolacion

#ejercicio calcular area y perimetro segun el alto y ancho que nos proporcione el usuario
altoCalculo = int(input('Escribir el alto: '))
anchoCalculo = int(input('Escribir el ancho: '))
calculoArea = altoCalculo * anchoCalculo
calculoPerimetro = (altoCalculo + anchoCalculo) * 2
print('Area calculada:', calculoArea, 'cm2')
print('Perimetro Calculado:', calculoPerimetro, 'cm')
print('Ejercicio terminado, facilito')

variableA = int(input('Escribe tu numero para saber si es par o impar: '))
boleanOfVariableA = variableA % 2 == 0
if boleanOfVariableA:
    print(f'Sii, {variableA} es un numerito par papu! Bien ahi ;)')
else:
    print(f'Nope! {variableA} no es par, proba con otro. :(')

rangeValue = int(input('Agrega un numero mayor a 0 y menor a 5: '))
mayor_menor = rangeValue <= 5 and rangeValue >= 0
if mayor_menor:
    print(f'{rangeValue} esta dentro del rango permitido')
else:
    print(f'claramente {rangeValue} no esta dentro del rango 0 a 5')
    print(f'Brother literalmente te escribi clarito que entre 0 y 5, no es tan dificil dea')


#SECCION 5 - ciclos loop

#ciclo while ejercicio, contador hasta 5
contador = 0
maximo = 5
while contador <= maximo:
    print(f'Contador: {contador}')
    contador += 1
else:
    print('Finalizo el algoritmo rey! first while loop in Python ;p')

#ciclo while ejercicio, contador descendente
minimo = 1
contadorDescendente = 5
while contadorDescendente >= minimo:
    print(f'Contador descendente: {contadorDescendente}')
    contadorDescendente -= 1
else:
    print('Finalizo el contador descendente!')

cadenaFor = "Python GOOOD"
contadorFor = 0
for letra in cadenaFor:
    print(f'Index {contadorFor}: {letra}')
    contadorFor += 1
else:
    print('Ciclo For finalizado!')

#break en ciclo for o while
cadenaForBreak = "Python GOOOD"
nuevaCadena = ""

for letra in cadenaForBreak:
    nuevaCadena += letra
    if letra == 'n':
        print(f'Esto es lo que se guardo de la cadena original: {nuevaCadena}')
        print('Solo queremos guardar python, no GOOOD')
        break
else:
    print('Ciclo For Break finalizado!')

#SECCION 6 - colecciones en python

#ejercicio 1 - iterar de 0 a 10, nums divisibles por 3
contadorRange10 = 0
for num in range(0, 11):
    print(f' iteracion {contadorRange10}/10')
    contadorRange10 += 1
    if num % 3 != 0:
        continue
    print(f'{num} es divisible por 3')

#ehercicio 2 - crear rango de 3 a 10 pero con salto de 2 en 2
for numJump in range(3, 11, 2):
    print(f'Numero {numJump}')

# set {'string random', otro string} - no tienen indices, pueden usarse en la funcion length
# tuplas ('Martin', 'Sofia', 'Luis') -> no pueden modificarse, inmutables, pero tienen los mismos metodos que una lista
# diccionario {'key': 'value', 'key2': 'value2'}, tiene metodos tambien
# listas/colecciones ['Martin', 'sofia'] -> son modificables y mutables, tambien tienen metodos


#SECCION 7 - funciones en python
def mi_primera_funcion():
    print('Soy la primera fucion en Python de Rodri! :)')

mi_primera_funcion()

def funcion_con_args(nombre, adjetivo = 'idolo'):
    print(f'Mi nombre es {nombre} y soy un {adjetivo}!')

funcion_con_args('Rodrigo', 'programador crack')

def funcion_suma(num1, num2):
    return num1 + num2

resultSumFunction = funcion_suma(10, 13)
print(f'El resultado de la funcion es: {resultSumFunction}')

def suma_argumentos(*numbArgs):
    newValueSumed = 0
    for num in numbArgs:
        newValueSumed += num
    return newValueSumed

print(suma_argumentos(10, 5, 5, 3))

def imprimir_diccionario(**kwargs):
    for key, value in kwargs.items():
        print(f'''
            Este es el key: {key}
            Este es el value: {value}
        ''')


print(imprimir_diccionario(RO = 'Rodrigo Orozco'))

def factorial_recursivo(numero):
    if numero == 1:
        return 1
    else:
        return numero * factorial_recursivo(numero - 1)

print(f'Este es el resultado factorial de 5: {factorial_recursivo(5)}')

def counter_recursive(number):
    if number <= 0:
        return number
    else:
        print(number)
        return counter_recursive(number - 1)

print(counter_recursive(5))
"""

#SECCION 8 - clases y objetos

# clase normal
class NewPersona:
    def __init__(self):
        self.nombre = 'Juan'
        self.apellido = 'Manresa'
        self.edad = 23

primeraClasePersona = NewPersona()
print(f'El nombre de la persona de mi primera clase es: {primeraClasePersona.nombre}')

# clase con argumentos
class NewPersonWithArgs():
    def __init__(self, nombre, apellido, edad):
        self.nombre = nombre
        self.apellido = apellido
        self.edad = edad

personaWithArgs = NewPersonWithArgs('Rodrigo', 'Orozco', 23)
print(f'El es {personaWithArgs.nombre}, su apellido es {personaWithArgs.apellido} y tiene {personaWithArgs.edad} años')
# cambio de atributos, ejemplo de porque es importante el encapsulamiento
personaWithArgs.nombre = 'Juan2'
personaWithArgs.apellido = 'Manresa2'
print(f'Se cambio su nombre a {personaWithArgs.nombre}, su apellido a {personaWithArgs.apellido} y sigue con {personaWithArgs.edad} años')

#metodos en clases
class PersonaConMetodo():
    def __init__(self, nombre, apellido, edad):
        self.nombre = nombre
        self.apellido = apellido
        self.edad = edad
    def mostrar_datos(self):
        print(f'{self.nombre} {self.apellido}, tiene {self.edad} años de edad!')

personaMuestraDetalle = PersonaConMetodo('Rodrigo', 'Orozco', 23)
personaMuestraDetalle.mostrar_datos() #forma 1
PersonaConMetodo.mostrar_datos(personaMuestraDetalle) #forma 2

class Aritmetica():
    def __init__(self, operandoA, operandoB):
        self.operandoA = operandoA
        self.operandoB = operandoB

    def sumar(self):
        return self.operandoA + self.operandoB
    def restar(self):
        return self.operandoA - self.operandoB
    def multiplicar(self):
        return self.operandoA * self.operandoB
    def dividir(self):
        return self.operandoA / self.operandoB

aritmetica1 = Aritmetica(5, 2)
print(f'Sumar: {aritmetica1.sumar()}')
print(f'Restar: {aritmetica1.restar()}')
print(f'Multiplicar: {aritmetica1.multiplicar()}')
print(f'Dividir: {aritmetica1.dividir():.2f}')

#EJERCICIO: crear clase con ancho y altura para calcular el area de un rectangulo, debe ser proporcionado por el usuario
class RectanguloCalculo():
    def __init__(self, alto, ancho):
        self.alto = alto
        self.ancho = ancho

    def calcular_area(self):
        return self.alto * self.ancho

#hacemos que el usuario proporcione los datos
altoCuadrado = int(input('Proporciona el alto del rectangulo: '))
anchoCuadrado = int(input('Proporciona el ancho del rectangulo: '))

#se lo proporcionamos a una variable que instancia la clase de rectangulo e imprimimos el calculo de su area automaticamente
calculoCuadrado = RectanguloCalculo(altoCuadrado, anchoCuadrado)
print(f'El area de tu rectangulo es: {calculoCuadrado.calcular_area()}')

class PersonaEncapsulada():
    def __init__(self, nombre, apellido, edad):
        self._nombre = nombre
        self._apellido = apellido
        self._edad = edad

    # GETTER method
    @property #Con este decorador deja de ser necesario llamar al metodo con (), se puede llamar como atributo
    def nombre(self):
        return self._nombre
    @property
    def apellido(self):
        return self._apellido

    #  SETTER method
    @nombre.setter
    def nombre(self, newNombre):
        self._nombre = newNombre
    @apellido.setter
    def apellido(self, newApellido):
        self._apellido = newApellido

    def __del__(self):
        print(f'Se elimino a {self._nombre} {self._apellido}')

