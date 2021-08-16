from mvc.view.tela_inicio_selecao_partida import TelaInicioSelecaoPartida
from mvc.control.controlador_jogador import ControladorJogador


class ControladorInicioSelecaoPartida:
    def __init__(self, controlador_principal):
        self.__controlador_principal = controlador_principal
        self.__tela_inicio_partida = TelaInicioSelecaoPartida(self)
        self.__controlador_jogador = ControladorJogador(self)

    def abre_tela_inicio_partida(self):
        button, values = self.__tela_inicio_partida.open_tela_inicio_selecao_partida()
        self.inicio_partida(values['oponente'], values['baralho'])
        if button == 'Voltar':
            self.__controlador_principal.abre_tela_inicial()

    def inicio_partida(self, oponente: str, baralho: str):
        print('entrou na função')
        print(oponente)
        print(baralho)
        if oponente == 'humano':
            self.__controlador_jogador.abre_tela_login()
