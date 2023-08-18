try:
    archivo = open('prueba.txt', 'r', encoding='utf8')
    #leer completo el archivo
    print(archivo.read())
    #leer caracteres
    #print(archivo.read(5))
    #leer lineas
    #print(archivo.readline())
except Exception as e:
    print(e)