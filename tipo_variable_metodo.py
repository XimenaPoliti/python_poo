class Gato():
    maullar = True

    def __init__(self, nombre, color):
        self.nombre = nombre
        self.color = color

    def descripcion(self, tamanio):
        print(f'Es de color {self.color} y {tamanio}')

    @classmethod
    def maullar(cls):
        print('miaw') if cls.maullar else print('UwU')

    @staticmethod
    def velocidad(es_veloz):
        print('muy veloz') if es_veloz else print('es lento')

    def prueba(self):
        self.descripcion('peque')
        self.maullar()
        self.velocidad(False)

    @classmethod
    def prueba_1(cls):
        gato = Gato('Kero', 'naranja')
        gato.descripcion('peque')
        cls.maullar()
        cls.velocidad(False)

    @staticmethod
    def prueba_2():
        gato = Gato('Kero', 'naranja')
        gato.descripcion('peque')
        Gato.maullar()
        Gato.velocidad(False)
        gato.maullar()
        gato.velocidad(True)


if __name__ == '__main__':
    print(Gato.maullar)
    gato = Gato('Feliz', 'negro')
    print(gato.nombre)
    gato.descripcion('grande')
    Gato.velocidad(False)
    Gato.maullar()
    gato.prueba()
    gato.velocidad(True)
    gato.maullar()
    Gato.prueba_1()
    Gato.prueba_2()
