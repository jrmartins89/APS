from mvc.view.tela_inicio_selecao_partida import TelaInicioSelecaoPartida
from mvc.control.controlador_jogador import ControladorJogador
from mvc.model.partida import Partida
from mvc.control.controlador_inteligencia_artificial import ControladorInteligenciaArtificial


class ControladorInicioSelecaoPartida:
    def __init__(self, controlador_principal):
        self.__controlador_principal = controlador_principal
        self.__tela_inicio_partida = TelaInicioSelecaoPartida(self)
        self.__controlador_jogador = ControladorJogador(self)
        self.__controlador_inteligencia_artifical = ControladorInteligenciaArtificial(self)
        self.__partida = []

    def abre_tela_inicio_partida(self, jogador_1):
        button, values = self.__tela_inicio_partida.open_tela_inicio_selecao_partida()
        tipo_oponente = values['oponente']
        if tipo_oponente == 'Computador':
            jogador_2 = self.__controlador_inteligencia_artifical.criar_inteligencia_artificial()
            self.inicio_partida(jogador_1, values['baralho'], jogador_2, 'Grego')
        elif tipo_oponente == 'Humano':
            jogador_2 = self.__controlador_jogador.abre_tela_login()
            self.inicio_partida(jogador_1, values['baralho'], jogador_2, 'Grego')
        if button == 'Voltar':
            self.__controlador_principal.abre_tela_inicial()

    def inicio_partida(self, jogador_1, tipo_baralho_1, jogador_2, tipo_baralho_2):
        self.__partida = Partida(jogador_1, tipo_baralho_1, jogador_2, tipo_baralho_2)
        print('imprimindo da partida')
        print('primeiro jogador é ' + self.__partida.jogador_1)
        print('segundo jogador é ' + self.__partida.jogador_2)
        print('baralho do primeiro jogador é ' + self.__partida.baralho_1)
        print('baralho do segundo jogador é ' + self.__partida.baralho_2)
