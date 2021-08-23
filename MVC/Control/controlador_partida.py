from mvc.control.controlador_jogador import ControladorJogador
from mvc.view.tela_partida import TelaPartida


class ControladorPartida:
    def __init__(self):
        self._tela_partida = TelaPartida(self)
        self._controlador_jogador = ControladorJogador(self)
        self._partida = None

    def abre_tela_confirmacao_partida_humano(self, partida):
        self._partida = partida
        button, values = self._tela_partida.open_confirmacao_partida_humano(self._partida)
        if button == 'Jogar!':
            self._tela_partida.open_jogo(self._partida)

    def abre_tela_confirmacao_partida_maquina(self, partida):
        self._partida = partida
        button, values = self._tela_partida.open_confirmacao_partida_maquina(self._partida)
        if button == 'Jogar!':
            self._tela_partida.open_jogo(self._partida)
