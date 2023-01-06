from loggin.logger_base import log

class Persona:
    def __init__(self, id_persona=None, nombre=None, apellido=None, gmail=None):
        self._id_persona = id_persona
        self._nombre = nombre
        self._apellido = apellido
        self._gmail = gmail

    def __str__(self):
        return f'''Persona[ID: {self._id_persona} ,Nombre: {self._nombre} ,Apellido: {self._apellido}, Gmail: {self._gmail}]'''

    # metodos get and set
    @property
    def nombre(self):
        return self._nombre

    @nombre.setter
    def nombre(self, nombre):
        self._nombre = nombre

    @property
    def apellido(self):
        return self._apellido

    @apellido.setter
    def apellido(self, apellido):
        self._apellido = apellido

    @property
    def gmail(self):
        return self._gmail

    @gmail.setter
    def gmail(self, gmail):
        self._gmail = gmail


if __name__ == '__main__':
    persona1 = Persona(None, "Chistian", "Palacios", 'Correo@correo.com')
    log.debug(persona1)

