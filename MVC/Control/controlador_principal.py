from MVC.View.tela_principal import TelaPrincipal
from MVC.Control.controlador_jogador import ControladorJogador


class ControladorPrincipal:

    def __init__(self):
        self.__tela = TelaPrincipal(self)
        self.__controlador_jogador = ControladorJogador(self)

    # para chamar a tela de jogadores é necessário pensar que o controlador da biblioteca conhece o controlador de usuários.

    # criando um laço de repeticao

    def abre_tela_inicial(self):
        while True:
            button, values = self.__tela.open_inicial()
            if button == 'Criar usuário':
                self.__controlador_jogador.abre_tela_cadastro()
            elif button == 'Log in':
                self.__controlador_jogador.abre_tela_login()
            self.__tela.open_principal()

    def abre_tela_principal(self):
        while True:
            button, values = self.__tela.open_principal()
            if button == 'Iniciar uma partida':
                self.__controlador_jogador.abre_tela_inicio_partida()
            elif button == 'Voltar':
                self.__tela.open_inicial()

    @property
    def controlador_jogador(self):
        return self.__controlador_jogador
