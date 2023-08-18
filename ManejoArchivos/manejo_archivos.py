try:
    archivo = open('prueba.txt', 'w', encoding='utf8')
    archivo.write('Cree un archivo txt desde el archivo py de manejo_Archivos :)\n')
    archivo.write('Voy a sobreescribir otra linea jeje')
except Exception as e:
    print(f'hubo una excepcion de tipo: {type(e)} y es: {e}')
finally:
    archivo.close()