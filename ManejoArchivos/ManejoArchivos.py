class ManejoArchivos:
    def __init__(self, name):
        self.name = name

    def __enter__(self):
        print('obtenemos el recurso'.center(50, '-'))
        self.name = open(self.name, 'r', encoding='utf8')
        return self.name

    def __exit__(self, exc_type, exc_val, exc_tb):
        print('cerramos el recurso'.center(50, '-'))
        if self.name:
            self.name.close()