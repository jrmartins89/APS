from MVC.Model.jogador_humano import JogadorHumano
from MVC.View.tela_login_jogador import TelaLoginJogador
from MVC.View.tela_cadastro_jogador import TelaCadastroJogador
import csv


class ControladorJogador:
    def __init__(self, controlador_principal):
        self.__controlador_principal = controlador_principal
        self.__tela_cadastro = TelaCadastroJogador(self)
        self.__tela_login = TelaLoginJogador(self)
        self.__jogadores = []

    def abre_tela_login(self):
        button, values = self.__tela_login.open_tela_login()
        self.fazer_login(values['apelido'], values['senha'])
        if button == 'Menu Principal':
            self.__controlador_principal.abre_tela()

    def abre_tela_cadastro(self):
        button, values = self.__tela_cadastro.open_tela_cadastro()
        self.incluir_usuario(values['nome'], values['apelido'], values['senha'])
        if button == 'Menu Principal':
            self.__controlador_principal.abre_tela()

    def incluir_usuario(self, nome: str, apelido: str, senha: int):
        cabecalho = ['nome', 'apelido', 'senha', 'da_vez', 'vitorias', 'derrotas', 'id_jogador']
        try:
            for jogador in self.__jogadores:
                if jogador.apelido == apelido:
                    raise Exception()
        except Exception:
            self.__tela_cadastro.show_message("Usuários", "Usuário já cadastrado no jogo")
        self.__jogadores.append(JogadorHumano(nome, apelido, senha, False, 0, 0, 1))
        with open('usuarios.csv', 'w', encoding='UTF8', newline='') as f:
            writer = csv.writer(f)
            writer.writerow(cabecalho)
            for jogador in self.__jogadores:
                writer.writerow([
                    jogador.nome,
                    jogador.apelido,
                    jogador.senha,
                    jogador.da_vez,
                    jogador.vitorias,
                    jogador.derrotas,
                    jogador.id_jogador])

        self.__tela_cadastro.show_message("CADASTRO DE USUÁRIOS", "Usuário cadastrado com sucesso!")

    def fazer_login(self, apelido: str, senha: int):
        with open('usuarios.csv', mode='r') as arquivo_csv:
            leitor_csv = csv.DictReader(arquivo_csv)
            for linha in leitor_csv:
                if (linha['apelido'] == apelido) & (linha['senha'] == senha):
                    self.__tela_login.show_message("LOGIN", "Login Realizado com sucesso!")
