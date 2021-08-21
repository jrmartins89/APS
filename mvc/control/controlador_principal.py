from mvc.view.tela_principal import TelaPrincipal
from mvc.view.tela_inicio_selecao_partida import TelaInicioSelecaoPartida
from mvc.control.controlador_jogador import ControladorJogador
from mvc.control.controlador_selecao_partida import ControladorInicioSelecaoPartida


class ControladorPrincipal:

    def __init__(self):
        self.__tela = TelaPrincipal(self)
        self.__tela_inicio_partida = TelaInicioSelecaoPartida(self)
        self.__controlador_jogador = ControladorJogador(self)
        self.__controlador_selecao_partida = ControladorInicioSelecaoPartida(self)

    # para chamar a tela de jogadores é necessário pensar que o controlador da
    # biblioteca conhece o controlador de usuários.

    # criando um laço de repeticao

    def abre_tela_inicial(self):
        while True:
            button, values = self.__tela.open_inicial()
            if button == 'Criar usuário':
                self.__controlador_jogador.abre_tela_cadastro()
            elif button == 'Login no Jogo':
                jogador_1 = self.__controlador_jogador.abre_tela_login()
                if jogador_1:
                    self.abre_tela_principal(jogador_1)

    def abre_tela_principal(self, jogador_1):
        while True:
            button, values = self.__tela.open_principal()
            if button == 'Iniciar uma partida':
                self.__controlador_selecao_partida.abre_tela_inicio_partida(jogador_1)
            elif button == 'Voltar':
                self.abre_tela_inicial()

    @property
    def controlador_jogador(self):
        return self.__controlador_jogador
