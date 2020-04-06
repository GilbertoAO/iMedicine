import shelve
from modelo import Remedio


def salva(remedio):
    arquivo = shelve.open("remedios")
    arquivo[remedio.nome] = remedio
    arquivo.close


def abre():
    arquivo = shelve.open("remedios")
    lista_remedios = list(arquivo.keys())
    remedios = [arquivo[remedio] for remedio in lista_remedios]
    arquivo.close
    return remedios
