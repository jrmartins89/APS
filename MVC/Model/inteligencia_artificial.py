class InteligenciaArtificial:
    def __init__(self, inteligencia_artificial):
        self.__inteligencia_artificial = inteligencia_artificial

    @property
    def inteligencia_artificial(self):
        return self.__inteligencia_artificial

    @inteligencia_artificial.setter
    def inteligencia_artificial(self, inteligencia_artificial):
        self.__inteligencia_artificial = inteligencia_artificial
