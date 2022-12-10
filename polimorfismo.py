class Persona:
    def __init__(self, nombre):
        self.nombre = nombre
        self._accion = 'Se desplaza caminando'

    def avanza(self):
        print(f'{self._accion}')


class Ciclista(Persona):

    def avanza(self):
        print('Se desplaza en bicicleta')


class Marinero(Persona):
    def __init__(self, nombre):
        super().__init__(nombre)
        self._accion = 'Se dezplaza en barco'

    def avanza(self):
        super().avanza()


def run():
    persona = Persona('Xime')
    persona.avanza()

    ciclista = Ciclista('Luna')
    ciclista.avanza()

    marinero = Marinero('Sol')
    marinero.avanza()

if __name__ == '__main__':
    run()
