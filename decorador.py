def decorador(funcion):
    def nueva_funcion(self, parametro):
        print('¡Buen día!')
        funcion(self, parametro)
    return nueva_funcion


class MiDecorador(object):
    def __init__(self, funcion):
        print('primero entrará en el init, esto pasa porque está siendo instanciado')
        self.funcion = funcion
        print('al crearse la clase Persona')

    def __call__(self):
        print('Gracias por la visita')
        self.funcion()
        print('¡Te deseo lo mejor!')
    

class MiDecoradorConArgumentos(object):
    def __init__(self, funcion):
        print('init con argumentos')
        self.funcion = funcion

    def __call__(self, *args,**kargs):
        self.funcion(*args,**kargs)
        print('¡funcion con argumentos!')


class Persona():
    
    def __init__(self, nombre):
        self.nombre = nombre

    @decorador
    def introduccion(self, ocupacion):
        self.ocupacion = ocupacion
        print(f'Mi nombre es {self.nombre}, soy {ocupacion}')

    @decorador
    def motivacion(self, accion):
        self.accion = accion
        print(f'Hoy es un día genial para {accion}')

    @MiDecorador
    def despedida():
        print('¡Hasta pronto!')

    @MiDecoradorConArgumentos
    def prueba(mensaje):
        print(f'¡prueba! {mensaje}')


if __name__ == '__main__':
    persona = Persona('Xime')
    persona.introduccion('artista')
    persona.motivacion('bailar')
    persona.despedida()
    persona.prueba('test')

