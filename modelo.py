from datetime import datetime


class Remedio:
    def __init__(self, nome, quantidade, periodo, tomou = list()):
        self._nome = nome
        self._quantidade = quantidade
        self._periodo = periodo
        self._tomou = tomou or list()

    def __str__(self):
        return f"{self._nome}: tomar {self._quantidade} comprimidos, a cada {self._periodo}h"

    def toma(self):
        self._tomou.append(datetime.today())

    @property
    def verifica_se_tomou_hoje(self):
        now = datetime.today()
        if len(self._tomou) > 1:
            return (
                self._tomou[-1].day == now.day
            )  ##to do: arrumar para frequeências maiores que uma vez por dia
        elif len(self._tomou) == 1:
            return self._tomou[0].day == now.day
        else:
            print("não tomou remédio pela primeira vez")
            return False

    @property
    def tomou(self):
        return self._tomou

    @property
    def nome(self):
        return self._nome

    @property
    def ultima_vez_que_tomou(self):
        if len(self._tomou) > 1:
            return str(self._tomou[-1])
        else:
            return str(self._tomou[0])


class ListaRemedios:
    def __init__(self, remedios):
        self._remedios = remedios

    def __getitem__(self, item):
        return self._remedios[item]

    def __str__(self):
        str_remedio = ""
        i = 1
        for remedio in self._remedios:
            str_remedio = f"{str_remedio} \n {i} - {remedio.nome} "
            i += 1
        return str_remedio
