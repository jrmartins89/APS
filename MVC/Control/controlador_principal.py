from MVC.View.tela_principal import TelaPrincipal
from MVC.Control.controlador_jogador import ControladorJogador


class ControladorPrincipal:

    def __init__(self):
        self.__tela = TelaPrincipal(self)
        self.__controlador_jogador = ControladorJogador(self)

    # para chamar a tela de jogadores é necessário pensar que o controlador da biblioteca conhece o controlador de usuários.

    # criando um laço de repeticao

    def abre_tela(self):
        while True:
            button, values = self.__tela.open()
            if button == 'Criar um novo usuário':
                self.__controlador_jogador.abre_tela_cadastro()
            elif button == 'Fazer login no jogo':
                self.__controlador_jogador.abre_tela_login()

    @property
    def controlador_jogador(self):
        return self.__controlador_jogador
