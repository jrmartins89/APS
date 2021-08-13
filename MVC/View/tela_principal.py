from MVC.View.tela import Tela
import PySimpleGUI as sg

sg.theme('DarkAmber')
font = ('Arial', '11', 'bold underline')
justification = 'center'

class TelaPrincipal(Tela):
    def __init__(self, controlador_principal):
        self.controlador_principal = controlador_principal
        self.__window_principal = None
        self.__hide = False

    def init_components(self):
        #sg.ChangeLookAndFeel('DarkAmber')
        layout_menu_principal = [
            [sg.Text('FÚRIA DOS PANTEÕES', font=(font, 20))],
            [sg.Text('Clique na opção desejada: ')],
            [sg.Button('Log in')],
            [sg.Button('Criar usuário')],
            [sg.Button('Iniciar uma partida')],
            [sg.Button('Glossário')],
            [sg.Button('Regras')],
            [sg.Button('Ranking')]
        ]
        self.__window_principal = sg.Window('Tela principal - Fúria dos Panteões').layout(layout_menu_principal)

    def open(self):
        self.init_components()
        button, values = self.__window_principal.read()
        self.close()
        return button, values

    def close(self):
        self.__window_principal.close()

    def show_message(self, titulo: str, mensagem: str):
        sg.Popup(titulo, mensagem)