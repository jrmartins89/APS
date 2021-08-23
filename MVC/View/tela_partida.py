from mvc.view.tela import Tela
import PySimpleGUI as sG

sG.theme('DarkAmber')


class TelaPartida(Tela):
    def __init__(self, controlador_partida):
        self.controlador_principal = controlador_partida
        self._window_confirmacao_partida_maquina = None
        self._window_confirmacao_partida_humano = None
        self._window_jogo = None
        self._hide = False
        self._partida = None

    def init_components_maquina(self):
        layout_confirmacao_partida_maquina = [
            [sG.Text('FÚRIA DOS PANTEÕES', font=('Times', 30))],
            [sG.Text('O primeiro jogador é ' + self._partida.jogador_1['apelido'])],
            [sG.Text('O segundo jogador é ' + self._partida.jogador_2.apelido)],
            [sG.Text('O baralho do primeiro jogador é ' + self._partida.baralho_1)],
            [sG.Text('O baralho do segundo jogador é ' + self._partida.baralho_2)],
            [sG.Button('Jogar!')]
        ]
        self._window_confirmacao_partida_maquina = sG.Window('Tela incial - Fúria dos Panteões',
                                                             font=('Times', 15),
                                                             size=(500, 250),
                                                             element_justification='c').layout(
            layout_confirmacao_partida_maquina)

    def init_components_humano(self):
        layout_confirmacao_partida_humano = [
            [sG.Text('FÚRIA DOS PANTEÕES', font=('Times', 30))],
            [sG.Text('O primeiro jogador é ' + self._partida.jogador_1['apelido'])],
            [sG.Text('O segundo jogador é ' + self._partida.jogador_2['apelido'])],
            [sG.Text('O baralho do primeiro jogador é do tipo ' + self._partida.baralho_1)],
            [sG.Text('O baralho do segundo jogador é do tipo ' + self._partida.baralho_2)],
            [sG.Button('Jogar!')]
        ]
        self._window_confirmacao_partida_humano = sG.Window('Tela incial - Fúria dos Panteões',
                                                            font=('Times', 15),
                                                            size=(500, 250),
                                                            element_justification='c').layout(
            layout_confirmacao_partida_humano)

    def init_jogo(self):
        layout_jogo = [
            [sG.Text('JOGO', font=('Times', 30))]

        ]
        self._window_jogo = sG.Window('Jogo',
                                      font=('Times', 15),
                                      size=(500, 250),
                                      element_justification='c').layout(
            layout_jogo)

    def open_confirmacao_partida_maquina(self, partida):
        self._partida = partida
        self.init_components_maquina()
        button, values = self._window_confirmacao_partida_maquina.Read()
        self.close_confirmacao_partida_maquina()
        return button, values

    def open_confirmacao_partida_humano(self, partida):
        self._partida = partida
        self.init_components_humano()
        button, values = self._window_confirmacao_partida_humano.Read()
        self.close_confirmacao_partida_humano()
        return button, values

    def open_jogo(self, partida):
        self.init_jogo()
        button, values = self._window_jogo.Read()
        self.close_jogo()
        return button, values

    def close_confirmacao_partida_humano(self):
        self._window_confirmacao_partida_humano.close()

    def close_jogo(self):
        self._window_jogo.close()

    def close_confirmacao_partida_maquina(self):
        self._window_confirmacao_partida_maquina.close()
