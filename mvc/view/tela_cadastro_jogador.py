from mvc.view.tela import Tela
import PySimpleGUI as sG

sG.theme('DarkAmber')


class TelaCadastroJogador(Tela):
    def __init__(self, controlador_jogador):
        self._controlador_jogador = controlador_jogador
        self._window_cadastro = None

    def init_components(self):
        layout_cadastro_jogador = [
                                    [sG.Text('Cadastro de Jogador', font=('Times', 30))],
                                    [sG.Text('Nome', font=('Times', 14))],
                                    [sG.InputText('', key='nome')],
                                    [sG.Text('*Apelido', font=('Times', 14))],
                                    [sG.InputText('', key='apelido')],
                                    [sG.Text('*Senha', font=('Times', 14))],
                                    [sG.InputText('', key='senha')],
                                    [sG.OK()],
                                    [sG.Button('Menu Principal')]
                                  ]

        self._window_cadastro = sG.Window('Cadastro de Jogador',
                                          font=('Times', 15),
                                          size=(600, 350),
                                          element_justification='c'
                                          ).Layout(layout_cadastro_jogador)

    def close(self):
        self._window_cadastro.Close()

    def open_tela_cadastro(self):
        self.init_components()
        button, values = self._window_cadastro.Read()
        self.close()
        return button, values

    def show_message(self, titulo: str, mensagem: str):
        sG.Popup(titulo, mensagem)
        self.close()
