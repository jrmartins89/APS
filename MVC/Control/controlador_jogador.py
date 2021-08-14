from MVC.Model.jogador_humano import JogadorHumano
from MVC.View.tela_login_jogador import TelaLoginJogador
from MVC.View.tela_cadastro_jogador import TelaCadastroJogador
import csv
import hashlib
import os


class ControladorJogador:
    def __init__(self, controlador_principal):
        self.__controlador_principal = controlador_principal
        self.__tela_cadastro = TelaCadastroJogador(self)
        self.__tela_login = TelaLoginJogador(self)
        self.__jogadores = []
        self.__idjogador = 0

    def abre_tela_login(self):
        button, values = self.__tela_login.open_tela_login()
        self.fazer_login(values['apelido'], values['senha'])
        if button == 'Voltar':
            self.__controlador_principal.abre_tela_inicial()

    def abre_tela_cadastro(self):
        button, values = self.__tela_cadastro.open_tela_cadastro()
        if button == 'Menu Principal':
            self.__controlador_principal.abre_tela_inicial()
        self.incluir_usuario(values['nome'], values['apelido'], values['senha'])

    def gerar_id(self):
        return

    def incluir_usuario(self, nome: str, apelido: str, senha: str):
        cabecalho = ['nome', 'apelido', 'senha', 'da_vez', 'vitorias', 'derrotas', 'id_jogador']
        if not apelido or apelido == '*Apelido':
            return self.__tela_cadastro.show_message("Erro", "O apelido não pode estar em branco.")
        if not senha or senha == '*Senha':
            return self.__tela_cadastro.show_message("Erro", "A senha não pode estar em branco.")

        try:
            for jogador in self.__jogadores:
                if jogador.apelido == apelido:
                    raise Exception()
        except Exception:
            return self.__tela_cadastro.show_message("Usuários", "Usuário já cadastrado.")
        self.__idjogador = self.__idjogador + 1
        self.__jogadores.append(JogadorHumano(nome, apelido, senha, False, 0, 0, self.__idjogador))
        with open('usuarios.csv', 'a', encoding='UTF-8', newline='') as f:
            for jogador in self.__jogadores:
                if len(jogador.senha) == 32:
                    continue
                hash_senha = jogador.senha.encode(encoding='UTF-8', errors='strict')
                hash_senha = hashlib.md5(hash_senha).hexdigest()
                jogador.senha = hash_senha
            writer = csv.writer(f)
            if os.stat('usuarios.csv').st_size == 0:
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
        self.__tela_cadastro.show_message("CADASTRO DE USUÁRIO", "Usuário cadastrado com sucesso!")

    def fazer_login(self, apelido: str, senha: str):
        login_inexistente = True
        with open('usuarios.csv', mode='r') as arquivo_csv:
            senha_fornecida = senha.encode(encoding='UTF-8', errors='strict')
            senha_fornecida = hashlib.md5(senha_fornecida).hexdigest()
            leitor_csv = csv.DictReader(arquivo_csv)
            while login_inexistente:
                for linha in leitor_csv:
                    if (linha['apelido'] == apelido) and (linha['senha'] == senha_fornecida):
                        self.__tela_login.show_message("SUCESSO", "Login Realizado com sucesso!")
                        login_inexistente = False
                if apelido == '':
                    break
                if login_inexistente:
                    self.__tela_login.show_message("ERRO", "Erro de Login!")
                    break
