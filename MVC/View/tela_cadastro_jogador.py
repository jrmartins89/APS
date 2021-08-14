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
