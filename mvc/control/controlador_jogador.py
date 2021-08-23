from mvc.model.jogador_humano import JogadorHumano
from mvc.model.jogador_maquina import JogadorMaquina
from mvc.view.tela_login_jogador import TelaLoginJogador
from mvc.view.tela_cadastro_jogador import TelaCadastroJogador
from mvc.view.tela_baralho_segundo_jogador import TelaBaralhoSegundoJogador
import csv
import hashlib
import os


class ControladorJogador:
    def __init__(self, controlador_principal):
        self.__controlador_principal = controlador_principal
        self.__tela_cadastro = TelaCadastroJogador(self)
        self.__tela_login = TelaLoginJogador(self)
        self.__tela_login_segundo_jogador = TelaLoginJogador(self)
        self.__jogador_maquina = None
        self.__tela_baralho_segundo_jogador = TelaBaralhoSegundoJogador(self)
        self.__jogadores = []
        self.__idjogador = 0

    def abre_tela_login(self):
        button, values = self.__tela_login.open_tela_login()
        verifica_login = self.fazer_login(values['apelido'], values['senha'])
        while not verifica_login:
            button, values = self.__tela_login.open_tela_login()
            verifica_login = self.fazer_login(values['apelido'], values['senha'])
        if button == 'Voltar':
            self.__controlador_principal.abre_tela_inicial()
        if (values['apelido'] == '') and (values['senha'] == ''):
            self.__tela_login.show_message("Erro", "O Login não pode ficar em branco!")
            return False
        else:
            return values['apelido']

    def abre_tela_login_segundo_jogador(self, jogador_1):
        button, values = self.__tela_login_segundo_jogador.open_tela_login_segundo_jogador()
        if values['apelido'] == jogador_1:
            self.__tela_login_segundo_jogador.show_message("Erro",
                                                           "O segundo jogador não pode ser igual ao primeiro jogador")
            return False
        if (values['apelido'] == '') and (values['senha'] == ''):
            self.__tela_login_segundo_jogador.show_message("Erro",
                                                           "O login não pode estar em branco!")
            return False
        else:
            verifica_login = self.fazer_login(values['apelido'], values['senha'])
        if verifica_login:
            return values['apelido']
        else:
            return False

    def abre_tela_baralho_segundo_jogador(self):
        button, values = self.__tela_baralho_segundo_jogador.open_tela_baralho_segundo_jogador()
        return values['baralho']

    def abre_tela_cadastro(self):
        button, values = self.__tela_cadastro.open_tela_cadastro()
        if button == 'Menu Principal':
            self.__controlador_principal.abre_tela_inicial()
        self.incluir_usuario_humano(values['nome'], values['apelido'], values['senha'])

    def gerar_id(self):
        return

    def inlcuir_usuario_maquina(self):
        self.__jogador_maquina = JogadorMaquina()
        return self.__jogador_maquina

    def incluir_usuario_humano(self, nome: str, apelido: str, senha: str):
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
                        self.__tela_login.show_message("SUCESSO!", apelido + " logado!")
                        login_inexistente = False
                if apelido == '':
                    break
                if login_inexistente:
                    self.__tela_login.show_message("ERRO", "Erro de Login!")
                    return False
            return True

    def criar_jogador_humano_memoria(self, jogador_1):
        with open('usuarios.csv', mode='r') as arquivo_csv:
            leitor_csv = csv.DictReader(arquivo_csv)
            for jogador in leitor_csv:
                if jogador_1 == jogador['apelido']:
                    JogadorHumano(jogador['nome'], jogador['apelido'], jogador['senha'], jogador['da_vez'],
                                  jogador['vitorias'], jogador['derrotas'], jogador['id_jogador'])
                    return jogador
