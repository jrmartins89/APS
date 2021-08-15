from MVC.View.tela import Tela
import PySimpleGUI as sG

sG.theme('DarkAmber')


class TelaInicioPartida(Tela):
    def __init__(self, controlador_principal):
        self.__controlador_principal = controlador_principal
        self.__window_inicio_partida = None
        self.__hide = False

    def init_components(self):
        layout_inicio_partida = [
                                    [sG.Text('Inicio da Partida', font=('Times', 30))],
                                    [sG.Text('Selecione o oponente', font=('Times', 14))],
                                    [sG.Combo(['humano', 'computador'], default_value='computador', key='oponente')],
                                    [sG.Text('Selecione o baralho', font=('Times', 14))],
                                    [sG.Combo(['Nordico', 'Egipcio', 'Grego'], default_value='Grego', key='baralho')],
                                    [sG.Text('Confirme a seleção', font=('Times', 14))],
                                    [sG.OK()],
                                    [sG.Button('Menu Principal')]
                                  ]

        self.__window_inicio_partida = sG.Window('Inicio da Partida',
                                                 font=('Times', 15),
                                                 size=(600, 300),
                                                 element_justification='c'
                                                 ).Layout(layout_inicio_partida)

    def close(self):
        self.__window_inicio_partida.close()

    def open_tela_inicio_partida(self):
        self.init_components()
        button, values = self.__window_inicio_partida.read()
        self.close()
        return button, values

    def show_message(self, titulo: str, mensagem: str):
        sG.Popup(titulo, mensagem)
        self.close()
