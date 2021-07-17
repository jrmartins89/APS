from abc import ABC, abstractmethod


class Jogador(ABC):
    @abstractmethod
    def __init__(self, da_vez, baralho, vitorias, derrotas):
        self.__da_vez = da_vez
        self.__baralho = baralho
        self.__vitorias = vitorias
        self.__derrotas = derrotas

    def mostra_lista_str(self, lista: []):
        for elem in lista:
            print(elem)
