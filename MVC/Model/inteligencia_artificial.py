class InteligenciaArtificial:
    def __init__(self):
        self._inteligencia_artificial = "inteligenciaArtificial"

    @property
    def inteligencia_artificial(self):
        return self._inteligencia_artificial

    @inteligencia_artificial.setter
    def inteligencia_artificial(self, inteligencia_artificial):
        self._inteligencia_artificial = inteligencia_artificial
