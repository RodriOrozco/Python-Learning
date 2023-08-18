from ManejoExcepeciones.ClasesExcepcionesPersonalizadas.NumerosIdenticosException import NumerosIdenticosException

resultado = None

try:
    a = int(input('Primer numero: '))
    b = int(input('Segundo numero: '))
    resultado = a/b
    #creamos una excepcion con una clase, en este caso si se colocan 2 numeros identicos tiramos un exception
    if a == b:
        raise NumerosIdenticosException('los numeros son identicos') #"rise" arroja las excepciones
#excepciones por errores y sus tipos
except ZeroDivisionError as zde:
    print(f'Zero division error: {zde}')
except TypeError as te:
    print(f'Type error: {te}')
except Exception as e:
    print(f'Ocurrio un error: {e}, type: {type(e)}')

#en caso de que no haya excepciones
else:
    print('no se arrojo ninguna excepcion')

# este se ejecuta sin importar si hay excepeciones o no
finally:
    print('finalizo el manejo de expeciones')

#----------------------------------------------------
print(f'Resultado: {resultado}')