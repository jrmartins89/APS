from MVC.Model.jogador import Jogador


class JogadorHumano(Jogador):
    def __init__(self, da_vez, baralho, vitorias, derrotas, senha, id_jogador, apelido):
        self.baralho = baralho
        self.__senha = senha
        self.__id_jogador = id_jogador
        self.__apelido = apelido
        self.__vitorias = vitorias
        self.__derrotas = derrotas
        self.__da_vez = da_vez

    @property
    def da_vez(self):
        return self.__da_vez

    @da_vez.setter
    def da_vez(self, da_vez: bool):
        if isinstance(da_vez, bool):
            self.__da_vez = da_vez

    @property
    def baralho(self):
        return self.__baralho

    @baralho.setter
    def baralho(self, baralho: baralho):
        if isinstance(baralho, baralho):
            self.__baralho = baralho

    @property
    def vitorias(self):
        return self.__vitorias

    @vitorias.setter
    def vitorias(self, vitorias: int):
        if isinstance(vitorias, int):
            self.__vitorias = vitorias

    @property
    def derrotas(self):
        return self.__derrotas

    @derrotas.setter
    def derrotas(self, derrotas: int):
        if isinstance(derrotas, int):
            self.__derrotas = derrotas

    @property
    def senha(self):
        return self.__senha

    @senha.setter
    def senha(self, senha: int):
        if isinstance(senha, int):
            self.__senha = senha

    @property
    def id_jogador(self):
        return self.__id_jogador

    @id_jogador.setter
    def id(self, id_jogador: str):
        if isinstance(id_jogador, str):
            self.__id_jogador = id

    @property
    def apelido(self):
        return self.__apelido

    @apelido.setter
    def apelido(self, apelido: str):
        if isinstance(apelido, str):
            self.__apelido = apelido