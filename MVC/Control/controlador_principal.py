from MVC.View.tela_principal import TelaPrincipal
from MVC.View.tela_inicio_partida import TelaInicioPartida
from MVC.Control.controlador_jogador import ControladorJogador


class ControladorPrincipal:

    def __init__(self):
        self.__tela = TelaPrincipal(self)
        self.__tela_inicio_partida = TelaInicioPartida(self)
        self.__controlador_jogador = ControladorJogador(self)

    # para chamar a tela de jogadores é necessário pensar que o controlador da
    # biblioteca conhece o controlador de usuários.

    # criando um laço de repeticao

    def abre_tela_inicial(self):
        while True:
            button, values = self.__tela.open_inicial()
            if button == 'Criar usuário':
                self.__controlador_jogador.abre_tela_cadastro()
            elif button == 'Login':
                fez_login = self.__controlador_jogador.abre_tela_login()
            if fez_login:
                self.abre_tela_principal()

    def abre_tela_principal(self):
        while True:
            button, values = self.__tela.open_principal()
            if button == 'Iniciar uma partida':
                self.__tela_inicio_partida.open_tela_inicio_partida()
            elif button == 'Voltar':
                self.__tela.open_inicial()

    @property
    def controlador_jogador(self):
        return self.__controlador_jogador
