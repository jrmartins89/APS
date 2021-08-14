from MVC.View.tela import Tela
import PySimpleGUI as sG

sG.theme('DarkAmber')
font = ('Arial', '11', 'bold underline')
justification = 'center'


class TelaPrincipal(Tela):
    def __init__(self, controlador_principal):
        self.controlador_principal = controlador_principal
        self.__window_inicial = None
        self.__window_principal = None
        self.__hide = False

    def init_components(self):
        #sg.ChangeLookAndFeel('DarkAmber')
        layout_menu_inicial = [
            [sG.Text('FÚRIA DOS PANTEÕES', font=(font, 20))],
            [sG.Text('Clique na opção desejada: ')],
            [sG.Button('Log in')],
            [sG.Button('Criar usuário')],
        ]
        self.__window_inicial = sG.Window('Tela incial - Fúria dos Panteões').layout(layout_menu_inicial)

    def init_full_components(self):
        #sg.ChangeLookAndFeel('DarkAmber')
        layout_menu_principal = [
            [sG.Text('FÚRIA DOS PANTEÕES', font=(font, 20))],
            [sG.Text('Clique na opção desejada: ')],
            [sG.Button('Iniciar uma partida')],
            [sG.Button('Voltar')]

        ]
        self.__window_principal = sG.Window('Tela principal - Fúria dos Panteões').layout(layout_menu_principal)

    def open_inicial(self):
        self.init_components()
        button, values = self.__window_inicial.read()
        self.close_inicial()
        return button, values

    def open_principal(self):
        self.init_full_components()
        button, values = self.__window_principal.read()
        self.close_principal()
        return button, values

    def close_principal(self):
        self.__window_principal.close()

    def close_inicial(self):
        self.__window_inicial.close()

    def show_message(self, titulo: str, mensagem: str):
        sG.Popup(titulo, mensagem)
