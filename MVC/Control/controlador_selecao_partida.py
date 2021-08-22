from mvc.view.tela_inicio_selecao_partida import TelaInicioSelecaoPartida
from mvc.control.controlador_jogador import ControladorJogador
from mvc.model.partida import Partida
from mvc.control.controlador_inteligencia_artificial import ControladorInteligenciaArtificial
from mvc.control.controlador_partida import ControladorPartida


class ControladorInicioSelecaoPartida:
    def __init__(self, controlador_principal):
        self.__controlador_principal = controlador_principal
        self.__tela_inicio_partida = TelaInicioSelecaoPartida(self)
        self.__controlador_jogador = ControladorJogador(self)
        self.__controlador_inteligencia_artifical = ControladorInteligenciaArtificial(self)
        self.__controlador_partida = ControladorPartida()
        self.__partida = []

        # função que enviará a chamada para o loop da partida
    def abre_tela_inicio_partida(self, jogador_1):
        button, values = self.__tela_inicio_partida.open_tela_inicio_selecao_partida()
        while (button == 'OK' and (values['baralho'] == '' and values['oponente'] == '')) or \
                (button == 'OK' and (values['baralho'] == '' or values['oponente'] == '')):
            self.__tela_inicio_partida.show_message("Erro", "As opções não podem ficar em branco!")
            button, values = self.__tela_inicio_partida.open_tela_inicio_selecao_partida()
        tipo_oponente = values['oponente']
        if tipo_oponente == 'Computador':
            jogador_2 = self.__controlador_jogador.inlcuir_usuario_maquina()
            self.inicio_partida_maquina(jogador_1, values['baralho'], jogador_2, 'Grego')
        elif tipo_oponente == 'Humano':
            jogador_2 = self.__controlador_jogador.abre_tela_login_segundo_jogador(jogador_1)
            while not jogador_2:
                jogador_2 = self.__controlador_jogador.abre_tela_login_segundo_jogador(jogador_1)
            baralho_2 = self.__controlador_jogador.abre_tela_baralho_segundo_jogador()
            self.inicio_partida_humano(jogador_1, values['baralho'], jogador_2, baralho_2)
        if button == 'Menu Principal':
            self.__controlador_principal.abre_tela_inicial()

    def inicio_partida_humano(self, jogador_1, tipo_baralho_1, jogador_2, tipo_baralho_2):
        jogador_1_memoria = self.__controlador_jogador.criar_jogador_humano_memoria(jogador_1)
        jogador_2_memoria = self.__controlador_jogador.criar_jogador_humano_memoria(jogador_2)
        self.__partida = Partida(jogador_1_memoria, tipo_baralho_1, jogador_2_memoria, tipo_baralho_2)
        self.__controlador_partida.abre_tela_confirmacao_partida_humano(self.__partida)
        print('imprimindo da partida')
        print('primeiro jogador é ' + self.__partida.jogador_1['apelido'])
        print('segundo jogador é ' + self.__partida.jogador_2['apelido'])
        print('baralho do primeiro jogador é do tipo ' + self.__partida.baralho_1)
        print('baralho do segundo jogador é do tipo  ' + self.__partida.baralho_2)

    def inicio_partida_maquina(self, jogador_1, tipo_baralho_1, jogador_2, tipo_baralho_2):
        jogador_1_memoria = self.__controlador_jogador.criar_jogador_humano_memoria(jogador_1)
        self.__partida = Partida(jogador_1_memoria, tipo_baralho_1, jogador_2, tipo_baralho_2)
        self.__controlador_partida.abre_tela_confirmacao_partida_maquina(self.__partida)
        print('imprimindo da partida')
        print('primeiro jogador é ' + self.__partida.jogador_1['apelido'])
        print('segundo jogador é ' + self.__partida.jogador_2.apelido)
        print('baralho do primeiro jogador é do tipo ' + self.__partida.baralho_1)
        print('baralho do segundo jogador é do tipo  ' + self.__partida.baralho_2)
