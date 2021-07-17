from MVC.Model.jogador import Jogador


class JogadorHumano(Jogador):
    def __init__(self, nome, apelido, senha, id_jogador):
        super().__init__(False, None, 0, 0)
        self.__nome = nome
        self.__apelido = apelido
        self.__senha = senha
        self.__id_jogador = id_jogador

    @property
    def nome(self):
        return self.__nome

    @nome.setter
    def nome(self, nome: str):
        if isinstance(nome, str):
            self.__nome = nome

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
    def id_jogador(self, id_jogador: str):
        if isinstance(id_jogador, str):
            self.__id_jogador = id_jogador

    @property
    def apelido(self):
        return self.__apelido

    @apelido.setter
    def apelido(self, apelido: str):
        if isinstance(apelido, str):
            self.__apelido = apelido
