from mvc.view.tela import Tela
import PySimpleGUI as sG

sG.theme('DarkAmber')


class TelaInicioSelecaoPartida(Tela):
    def __init__(self, controlador_principal):
        self._controlador_principal = controlador_principal
        self._window_inicio_selecao_partida = None
        self._hide = False

    def init_components(self):
        layout_inicio_selecao_partida = [
                                    [sG.Text('Início da Partida', font=('Times', 30))],
                                    [sG.Text('Selecione o seu oponente', font=('Times', 14))],
                                    [sG.Combo(['Humano', 'Computador'], key='oponente')],
                                    [sG.Text('Selecione o seu tipo de baralho', font=('Times', 14))],
                                    [sG.Combo(['Nórdico', 'Egípcio', 'Grego'], key='baralho')],
                                    [sG.Text('Confirme a seleção', font=('Times', 14))],
                                    [sG.OK()],
                                    [sG.Button('Menu Principal')]
                                  ]

        self._window_inicio_selecao_partida = sG.Window('Início da Partida',
                                                        font=('Times', 15),
                                                        size=(600, 300),
                                                        element_justification='c'
                                                        ).Layout(layout_inicio_selecao_partida)

    def close(self):
        self._window_inicio_selecao_partida.close()

    def open_tela_inicio_selecao_partida(self):
        self.init_components()
        button, values = self._window_inicio_selecao_partida.read()
        self.close()
        return button, values

    def show_message(self, titulo: str, mensagem: str):
        sG.Popup(titulo, mensagem)
        self.close()
