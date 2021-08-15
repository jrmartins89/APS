from mvc.view.tela import Tela
import PySimpleGUI as sG

sG.theme('DarkAmber')


class TelaLoginJogador(Tela):
    def __init__(self, controlador_jogador):
        self.__controlador_jogador = controlador_jogador
        self.__window_login = None

    def init_components(self):
        layout_login_jogador = [
                                    [sG.Text('Faça o login!', font=('Times', 30))],
                                    [sG.Text('*Apelido', font=('Times', 14))],
                                    [sG.InputText('', key='apelido')],
                                    [sG.Text('*Senha', font=('Times', 14))],
                                    [sG.InputText('', key='senha')],
                                    [sG.OK()],
                                    [sG.Button('Voltar')]
                               ]

        self.__window_login = sG.Window('Login no Jogo',
                                        font=('Times', 15),
                                        size=(600, 300),
                                        element_justification='c'
                                        ).Layout(layout_login_jogador)

    def close(self):
        self.__window_login.Close()

    def open_tela_login(self):
        self.init_components()
        button, values = self.__window_login.Read()
        self.close()
        return button, values

    def show_message(self, titulo: str, mensagem: str):
        sG.Popup(titulo, mensagem)
        self.close()
