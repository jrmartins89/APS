from MVC.View.tela import Tela
import PySimpleGUI as sg

sg.theme('DarkAmber')
font = ('Arial', '11', 'bold underline')
justification = 'center'

class TelaLoginJogador(Tela):
    def __init__(self, controlador_jogador):
        self.__controlador_jogador = controlador_jogador
        self.__window_login = None

    def init_components(self):
        layout_login_jogador = [
                                    [sg.Text('Faça o login!')],
                                    [sg.InputText('*Apelido', key='apelido')],
                                    [sg.InputText('*Senha ', key='senha')],
                                    [sg.OK()],
                                    [sg.Text('Não possui uma conta ainda?', key = '-text-')],
                                    [sg.Button('Voltar')]
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
        self.close()
