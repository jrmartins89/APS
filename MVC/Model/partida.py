class Partida:
    def __init__(self, jogador_1: str, jogador_2: str):
        self.__jogador_1 = jogador_1
        self.__jogador_2 = jogador_2
        self.__baralho = None

    @property
    def jogador_1(self):
        return self.__jogador_1

    @jogador_1.setter
    def jogador_1(self, jogador_1: str):
        self.__jogador_1 = jogador_1

    @property
    def jogador_2(self):
        return self.__jogador_2

    @jogador_2.setter
    def jogador_2(self, jogador_2: str):
        self.__jogador_2 = jogador_2

    @property
    def baralho(self):
        return self.__baralho

    @baralho.setter
    def baralho(self, baralho: str):
        self.__baralho = baralho
