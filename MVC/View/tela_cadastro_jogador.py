from MVC.View.tela import Tela
import PySimpleGUI as sg

sg.theme('DarkAmber')
font = ('Arial', '11', 'bold underline')
justification = 'center'

class TelaCadastroJogador(Tela):
    def __init__(self, controlador_jogador):
        self.__controlador_jogador = controlador_jogador
        self.__window_cadastro = None

    def init_components(self):
        layout_cadastro_jogador = [
                                    [sg.Text('Cadastro de Jogador')],
                                    [sg.InputText('*Nome', key='nome')],
                                    [sg.InputText('*Apelido', key='apelido')],
                                    [sg.InputText('*Senha', key='senha')],
                                    [sg.OK()],
                                    [sg.Button('Menu Principal')]
                                  ]

        self.__window_cadastro = sg.Window('Cadastro de Jogador').Layout(layout_cadastro_jogador)

    def close(self):
        self.__window_cadastro.Close()

    def open_tela_cadastro(self):
        self.init_components()
        button, values = self.__window_cadastro.Read()
        self.close()
        return button, values

    def show_message(self, titulo: str, mensagem: str):
        sg.Popup(titulo, mensagem)
        self.close()


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