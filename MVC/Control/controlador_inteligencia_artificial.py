from mvc.model.inteligencia_artificial import InteligenciaArtificial


class ControladorInteligenciaArtificial:
    def __init__(self, controlador_selecao_partida):
        self._controlador_selecao_partida = controlador_selecao_partida
        self._inteligencia_artificial = InteligenciaArtificial()

    def criar_inteligencia_artificial(self):
        print(self._inteligencia_artificial)
        return self._inteligencia_artificial.inteligencia_artificial
