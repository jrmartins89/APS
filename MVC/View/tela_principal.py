from view.tela import Tela
import PySimpleGUI as sg


class TelaBiblioteca(Tela):
    def __init__(self, controlador_biblioteca):
        self.controlador_biblioteca = controlador_biblioteca
        self.__window = None
        self.__hide = False

    def init_components(self):
        sg.ChangeLookAndFeel('SandyBeach')
        layout_menu_biblioteca = [
            [sg.Text('----- Bem Vindo à biblioteca gamer! -----')],
            [sg.Text('Clique na opção desejada: ')],
            [sg.Button('Menu de Usuários')],
            [sg.Button('Menu de Jogos')],
            [sg.Button('Menu de Aquisições')]
            ]
        self.__window = sg.Window('Menu da Biblioteca').layout(layout_menu_biblioteca)

    def open(self):
        self.init_components()
        button, values = self.__window.read()
        self.close()
        return button, values

    def close(self):
        self.__window.close()

    def show_message(self, titulo: str, mensagem: str):
        sg.Popup(titulo, mensagem)
