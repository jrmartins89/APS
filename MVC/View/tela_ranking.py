from mvc.view.tela import Tela
import PySimpleGUI as sG
import pandas as pd

sG.theme('DarkAmber')


class TelaRanking(Tela):
    def __init__(self, controlador_principal):
        self.controlador_principal = controlador_principal
        self._window_ranking = None
        self._hide = False
        self._jogadores = None

    def init_components(self):
        layout_ranking = [
            [sG.Text('RANKING', font=('Times', 30))],
            [sG.Text(self._jogadores.to_string(index=False))],
            [sG.Quit('Sair')]
        ]
        self._window_ranking = sG.Window('Tela Ranking - Fúria dos Panteões',
                                         font=('Times', 15),
                                         size=(500, 350),
                                         element_justification='c').layout(layout_ranking)

    def open_ranking(self):
        col_list = ["apelido", "vitorias", "derrotas"]
        self._jogadores = pd.read_csv("usuarios.csv", usecols=col_list)
        print(self._jogadores.to_string(index=False))
        self.init_components()
        button, values = self._window_ranking.read()
        self.close_ranking()
        return button, values

    def close_ranking(self):
        self._window_ranking.Close()

    def show_message(self, titulo: str, mensagem: str):
        sG.Popup(titulo, mensagem)
