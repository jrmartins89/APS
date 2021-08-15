from mvc.view.tela_inicio_partida import TelaInicioPartida


class ControladorInicioPartida:
    def __init__(self, controlador_principal):
        self.__controlador_principal = controlador_principal
        self.__tela_inicio_partida = TelaInicioPartida(self)

    def abre_tela_inicio_partida(self):
        button, values = self.__tela_inicio_partida.open_tela_inicio_partida()
        print(values)
        if button == 'Voltar':
            self.__controlador_principal.abre_tela_inicial()
