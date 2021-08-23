from mvc.model.jogador import Jogador


class JogadorHumano(Jogador):
    def __init__(self, nome, apelido, senha, da_vez, vitorias, derrotas, id_jogador=0):
        self._nome = nome
        self._apelido = apelido
        self._senha = senha
        self._da_vez = da_vez
        self._vitorias = vitorias
        self._derrotas = derrotas
        self._id_jogador = id_jogador

    @property
    def nome(self):
        return self._nome

    @nome.setter
    def nome(self, nome: str):
        if isinstance(nome, str):
            self._nome = nome

    @property
    def da_vez(self):
        return self._da_vez

    @da_vez.setter
    def da_vez(self, da_vez: bool):
        if isinstance(da_vez, bool):
            self._da_vez = da_vez

    @property
    def vitorias(self):
        return self._vitorias

    @vitorias.setter
    def vitorias(self, vitorias: int):
        if isinstance(vitorias, int):
            self._vitorias = vitorias

    @property
    def derrotas(self):
        return self._derrotas

    @derrotas.setter
    def derrotas(self, derrotas: int):
        if isinstance(derrotas, int):
            self._derrotas = derrotas

    @property
    def senha(self):
        return self._senha

    @senha.setter
    def senha(self, senha: str):
        if isinstance(senha, str):
            self._senha = senha

    @property
    def id_jogador(self):
        return self._id_jogador

    @id_jogador.setter
    def id_jogador(self, id_jogador: str):
        if isinstance(id_jogador, str):
            self._id_jogador = id_jogador

    @property
    def apelido(self):
        return self._apelido

    @apelido.setter
    def apelido(self, apelido: str):
        if isinstance(apelido, str):
            self._apelido = apelido
