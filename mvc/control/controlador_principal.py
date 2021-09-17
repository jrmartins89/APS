from mvc.view.tela_principal import TelaPrincipal
from mvc.view.tela_inicio_selecao_partida import TelaInicioSelecaoPartida
from mvc.control.controlador_jogador import ControladorJogador
from mvc.control.controlador_selecao_partida import ControladorInicioSelecaoPartida
# from mvc.view.jogoloop import *


class ControladorPrincipal:

    def __init__(self):
        self._tela = TelaPrincipal(self)
        self._tela_inicio_partida = TelaInicioSelecaoPartida(self)
        self._controlador_jogador = ControladorJogador(self)
        self._controlador_selecao_partida = ControladorInicioSelecaoPartida(self)
        #self._jogo = JogoLoop(Self)
    # para chamar a tela de jogadores é necessário pensar que o controlador da
    # biblioteca conhece o controlador de usuários.

    # criando um laço de repeticao

    def abre_tela_inicial(self):
        while True:
            button, values = self._tela.open_inicial()
            if button == 'Criar Usuário':
                self._controlador_jogador.abre_tela_cadastro()
            elif button == 'Realizar Login':
                jogador_1 = self._controlador_jogador.abre_tela_login()
                if jogador_1:
                    self.abre_tela_principal(jogador_1)
            elif button == 'Sair':
                break

    def abre_tela_principal(self, jogador_1):
        button, values = self._tela.open_principal()
        if button == 'Iniciar uma partida':
            self._controlador_selecao_partida.abre_tela_inicio_partida(jogador_1)
        elif button == 'Voltar':
            self.abre_tela_inicial()
        elif button == 'Sair':
            exit(0)

    @property
    def controlador_jogador(self):
        return self._controlador_jogador
