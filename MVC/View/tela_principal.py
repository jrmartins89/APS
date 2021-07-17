from MVC.View.tela import Tela
import PySimpleGUI as sg


class TelaPrincipal(Tela):
    def __init__(self, controlador_principal):
        self.controlador_principal = controlador_principal
        self.__window_principal = None
        self.__hide = False

    def init_components(self):
        sg.ChangeLookAndFeel('SandyBeach')
        layout_menu_principal = [
            [sg.Text('----- Bem Vindo à Fúria dos Panteões! -----')],
            [sg.Text('Clique na opção desejada: ')],
            [sg.Button('Fazer login no jogo')],
            [sg.Button('Criar um novo usuário')]
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