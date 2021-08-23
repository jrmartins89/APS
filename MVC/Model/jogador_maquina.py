from mvc.model.jogador import Jogador
from mvc.model.inteligencia_artificial import InteligenciaArtificial


class JogadorMaquina(Jogador):
    def __init__(self):
        self._apelido = 'jogador_maquina'
        self._inteligencia_artificial = InteligenciaArtificial()

    @property
    def apelido(self):
        return self._apelido

    @apelido.setter
    def apelido(self, apelido):
        self._apelido = apelido

    @property
    def inteligencia_artificial(self):
        return self._inteligencia_artificial

    @inteligencia_artificial.setter
    def inteligencia_artificial(self, inteligencia_artificial):
        self._inteligencia_artificial = inteligencia_artificial
