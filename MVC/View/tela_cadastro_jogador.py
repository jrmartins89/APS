from MVC.View.tela import Tela
import PySimpleGUI as sg


class TelaCadastroJogador(Tela):
    def __init__(self, controlador_jogador):
        self.__controlador_jogador = controlador_jogador
        self.__window_cadastro = None

    def init_components(self):
        sg.ChangeLookAndFeel('SandyBeach')
        layout_cadastro_jogador = [
                                    [sg.Text('Cadastro de um novo jogador')],
                                    [sg.InputText('Nome', key='nome')],
                                    [sg.InputText('Apelido', key='apelido')],
                                    [sg.InputText('Senha (Apenas números)', key='senha')],
                                    [sg.Submit()]
                                  ]

        self.__window_cadastro = sg.Window('Cadastro de Jogador').Layout(layout_cadastro_jogador)

    def close(self):
        self.__window_cadastro.Close()

    def open_tela_cadastro(self):
        self.init_components()
        return self.__window_cadastro.Read()

    def show_message(self, titulo: str, mensagem: str):
        sg.Popup(titulo, mensagem)


"""
     esse método recebe uma lista como parametro, percorre ela e exibe os elementos da mesma
    def exibir_menu_opcoes(self, lista: []):
       for elem in lista:
            print(elem)

    def verifica_opcao(self, msg: str = "", opcoes_validas: [] = None):
        while True:
            valor_lido = input(msg)
            try:
               inteiro = int(valor_lido)
               if opcoes_validas and inteiro not in opcoes_validas:
                   raise ValueError
               return inteiro
           except ValueError:
               print("Digite uma opção válida.")

    def tratar_int_str(self, msg=""):
        while True:
            try:
                resposta = int(input(msg))
                return resposta
            except ValueError:
"""