from mvc.model.inteligencia_artificial import InteligenciaArtificial


class ControladorInteligenciaArtificial:
    def __init__(self, controlador_selecao_partida):
        self.__controlador_selecao_partida = controlador_selecao_partida
        self.__inteligencia_artificial = InteligenciaArtificial()

    def criar_inteligencia_artificial(self):
        print(self.__inteligencia_artificial)
        return self.__inteligencia_artificial.inteligencia_artificial
