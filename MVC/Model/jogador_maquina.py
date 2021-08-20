from mvc.model.jogador import Jogador
from mvc.model.inteligencia_artificial import InteligenciaArtificial


class JogadorMaquina(Jogador):
    def __init__(self):
        self.__apelido = 'jogador_maquina'
        self.__inteligencia_artificial = InteligenciaArtificial()

    @property
    def apelido(self):
        return self.__apelido

    @apelido.setter
    def apelido(self, apelido):
        self.__apelido = apelido

    @property
    def inteligencia_artificial(self):
        return self.__inteligencia_artificial

    @inteligencia_artificial.setter
    def inteligencia_artificial(self, inteligencia_artificial):
        self.__inteligencia_artificial = inteligencia_artificial
