class Partida:
    def __init__(self, jogador_1, tipo_baralho_1, jogador_2, tipo_baralho_2):
        self.__jogador_1 = jogador_1
        self.__jogador_2 = jogador_2
        self.__baralho_1 = tipo_baralho_1
        self.__baralho_2 = tipo_baralho_2

    @property
    def jogador_1(self):
        return self.__jogador_1

    @jogador_1.setter
    def jogador_1(self, jogador_1):
        self.__jogador_1 = jogador_1

    @property
    def jogador_2(self):
        return self.__jogador_2

    @jogador_2.setter
    def jogador_2(self, jogador_2):
        self.__jogador_2 = jogador_2

    @property
    def baralho_1(self):
        return self.__baralho_1

    @baralho_1.setter
    def baralho_1(self, baralho_1):
        self.__baralho_1 = baralho_1

    @property
    def baralho_2(self):
        return self.__baralho_2

    @baralho_2.setter
    def baralho_2(self, baralho_2):
        self.__baralho_2 = baralho_2
