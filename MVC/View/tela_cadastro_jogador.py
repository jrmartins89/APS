from MVC.View.tela import Tela
import PySimpleGUI as sG

sG.theme('DarkAmber')
font = ('Arial', '11', 'bold underline')
justification = 'center'


class TelaCadastroJogador(Tela):
    def __init__(self, controlador_jogador):
        self.__controlador_jogador = controlador_jogador
        self.__window_cadastro = None

    def init_components(self):
        layout_cadastro_jogador = [
                                    [sG.Text('Cadastro de Jogador')],
                                    [sG.Text('Nome')],
                                    [sG.InputText('', key='nome')],
                                    [sG.Text('*Apelido')],
                                    [sG.InputText('', key='apelido')],
                                    [sG.Text('*Senha')],
                                    [sG.InputText('', key='senha')],
                                    [sG.OK()],
                                    [sG.Button('Menu Principal')]
                                  ]

        self.__window_cadastro = sG.Window('Cadastro de Jogador').Layout(layout_cadastro_jogador)

    def close(self):
        self.__window_cadastro.Close()

    def open_tela_cadastro(self):
        self.init_components()
        button, values = self.__window_cadastro.Read()
        self.close()
        return button, values

    def show_message(self, titulo: str, mensagem: str):
        sG.Popup(titulo, mensagem)
        self.close()
