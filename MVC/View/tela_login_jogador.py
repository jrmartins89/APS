from MVC.View.tela import Tela
import PySimpleGUI as sg


class TelaLoginJogador(Tela):
    def __init__(self, controlador_jogador):
        self.__controlador_jogador = controlador_jogador
        self.__window_login = None

    def init_components(self):
        sg.ChangeLookAndFeel('SandyBeach')
        layout_login_jogador = [
                                    [sg.Text('Faça o login no jogo!')],
                                    [sg.InputText('*Apelido', key='apelido')],
                                    [sg.InputText('*Senha (Apenas números) ', key='senha')],
                                    [sg.Submit()],
                                    [sg.Button('Menu Principal')]
                               ]

        self.__window_login = sg.Window('Login no Jogo').Layout(layout_login_jogador)

    def close(self):
        self.__window_login.Close()

    def open_tela_login(self):
        self.init_components()
        button, values = self.__window_login.Read()
        self.close()
        return button, values

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