from mvc.control.controlador_jogador import ControladorJogador
from mvc.view.tela_partida import TelaPartida


class ControladorPartida:
    def __init__(self):
        self.__tela_partida = TelaPartida(self)
        self.__controlador_jogador = ControladorJogador(self)
        self.__partida = None

    def abre_tela_confirmacao_partida_humano(self, partida):
        self.__partida = partida
        self.__tela_partida.open_confirmacao_partida_humano(self.__partida)

    def abre_tela_confirmacao_partida_maquina(self, partida):
        self.__partida = partida
        button, values = self.__tela_partida.open_confirmacao_partida_maquina(self.__partida)
        if button == 'Jogar!':
            self.__tela_partida.open_jogo(self.__partida)
