from abc import ABC, abstractmethod


class Jogador(ABC):
    @abstractmethod
    def __init__(self, da_vez, baralho, vitorias, derrotas):
        pass

    def mostra_lista_str(self, lista: []):
        for elem in lista:
            print(elem)
