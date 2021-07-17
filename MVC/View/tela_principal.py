from MVC.View.tela import Tela
import PySimpleGUI as sG


class TelaPrincipal(Tela):
    def __init__(self, controlador_principal):
        self.controlador_principal = controlador_principal
        self.__window_principal = None
        self.__hide = False

    def init_components(self):
        sG.ChangeLookAndFeel('SandyBeach')
        layout_menu_principal = [
            [sG.Text('----- Bem Vindo à Fúria dos Panteões! -----')],
            [sG.Text('Clique na opção desejada: ')],
            [sG.Button('Fazer login no jogo')],
            [sG.Button('Criar um novo usuário')]
        ]
        self.__window_principal = sG.Window('Tela principal - Fúria dos Panteões').layout(layout_menu_principal)

    def open(self):
        self.init_components()
        button, values = self.__window_principal.read()
        self.close()
        return button, values

    def close(self):
        self.__window_principal.close()
