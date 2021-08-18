class InteligenciaArtificial:
    def __init__(self):
        self.__inteligencia_artificial = "inteligenciaArtificial"


    @property
    def inteligencia_artificial(self):
        return self.__inteligencia_artificial

    @inteligencia_artificial.setter
    def inteligencia_artificial(self, inteligencia_artificial):
        self.__inteligencia_artificial = inteligencia_artificial
