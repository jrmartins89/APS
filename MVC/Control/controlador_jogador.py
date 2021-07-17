from MVC.Model.jogador_humano import JogadorHumano
from MVC.View.tela_login_jogador import TelaLoginJogador
from MVC.View.tela_cadastro_jogador import TelaCadastroJogador


class ControladorJogador:
    def __init__(self, controlador_principal):
        self.__controlador_principal = controlador_principal
        self.__tela_cadastro = TelaCadastroJogador(self)
        self.__tela_login = TelaLoginJogador(self)
        self.__jogadores = []

    def abre_tela_login(self):
        button, values = self.__tela_login.open_tela_login()
        self.fazer_login(values['Apelido'], values['senha'])
        if button == 'Voltar ao menu principal':
            self.__controlador_principal.abre_tela()

    def abre_tela_cadastro(self):
        button, values = self.__tela_cadastro.open_tela_cadastro()
        self.incluir_usuario(values['Nome'], values['Apelido'], values['Senha'])
        if button == 'Voltar ao menu principal':
            self.__controlador_jogador.abre_tela()

    def incluir_usuario(self, nome: str, apelido: str, senha: int):
        try:
            for jogador in self.__jogadores:
              if jogador.apelido == apelido:
                raise Exception()
        except Exception:
            self.__tela_cadastro.show_message("Usuários", "Usuário já existente no sistema")
        else:
            self.__jogadores.append(JogadorHumano(nome, apelido, senha, False, None, 0, 0, 1))
            self.__tela_cadastro.show_message("CADASTRO DE USUÁRIOS", "Usuário cadastrado com sucesso!")

    def fazer_login(self, apelido: str, senha: int):
        button, values = self.__tela_login.open_tela_login()
