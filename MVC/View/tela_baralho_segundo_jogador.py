from mvc.view.tela import Tela
import PySimpleGUI as sG

sG.theme('DarkAmber')


class TelaBaralhoSegundoJogador(Tela):
    def __init__(self, controlador_jogador):
        self.__controlador_jogador = controlador_jogador
        self.__window_baralho_segundo_jogador = None
        self.__hide = False

    def init_components(self):
        layout_baralho_segundo_jogador = [
            [sG.Text('Início da Partida - Segundo Jogador', font=('Times', 30))],
            [sG.Text('Selecione o seu tipo de baralho', font=('Times', 14))],
            [sG.Combo(['Nórdico', 'Egípcio', 'Grego'], default_value='Grego', key='baralho')],
            [sG.Text('Confirme a seleção', font=('Times', 14))],
            [sG.OK()],
            [sG.Button('Voltar')]
        ]

        self.__window_baralho_segundo_jogador = sG.Window('Início da Partida',
                                                          font=('Times', 15),
                                                          size=(600, 300),
                                                          element_justification='c'
                                                          ).Layout(layout_baralho_segundo_jogador)

    def close(self):
        self.__window_baralho_segundo_jogador.close()

    def open_tela_baralho_segundo_jogador(self):
        self.init_components()
        button, values = self.__window_baralho_segundo_jogador.read()
        self.close()
        return button, values

    def show_message(self, titulo: str, mensagem: str):
        sG.Popup(titulo, mensagem)
        self.close()
