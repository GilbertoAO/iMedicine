from modelo import Remedio, ListaRemedios
from armazenamento import abre, salva, exclui


def carrega():
    return abre()


def input_inicio():
    print("###################################################")
    print("############ Menu 1: O que deseja fazer? ##########")
    print("###################################################")
    print("1 - Cadastrar um novo remédio")
    print("2 - Consultar informações de remédio cadastrado")
    print("3 - Confirmar que tomou")
    print("4 - Excluir o cadastro de um remédio")   
    print("5 - encerrar")    
    controle = input()    
    return controle


def add_remedio():
    print("Cadastro de novo remédio")
    nome_remedio = input("Nome do remédio: ")
    quantidade = input("dose: ")
    periodo = input("Tomar remédio a cada quantas horas?")
    novo_remedio = Remedio(nome_remedio, quantidade, periodo)
    print(novo_remedio)
    salva(novo_remedio)
    input("Aperte enter para continuar")
    return novo_remedio


def mostra_remedio():
    print("escolha uma opção:")
    todos_remedios = carrega()
    print(ListaRemedios(todos_remedios))
    controle = int(input())
    return todos_remedios[controle - 1]


def tomou():


    print("informar que tomou remédio. ")
    remedio = mostra_remedio()
    remedio.toma()
    salva(remedio)
    input("Informação registrada. Enter para continuar...")


def verifica_se_tomou():
    remedio = mostra_remedio()
    if remedio.verifica_se_tomou_hoje:
        print(f"Você já tomou o remédio hoje: {remedio.ultima_vez_que_tomou}")
    else:
        print(f"Você ainda não tomou o remédio hoje:  {remedio.ultima_vez_que_tomou}")

def exclui_remedio():
    print("Excluindo remédio...")
    remedio = mostra_remedio()
    key_remedio = remedio.nome
    exclui(key_remedio)
    input("Remédio excluido com sucesso. Enter para continuar")


def rotina_inicial():
    rodando = True
    while rodando:
        controle = input_inicio()
        if controle == "1":
            add_remedio()
        elif controle == "2":
            print("###################################################")
            print("############ Menu 1: O que deseja fazer? ##########")
            print("###################################################")
            print("1 - Verificar se tomou")
            print("2 - Apenas visualizar informações")
            control2 = input()
            if control2 == "1":
                verifica_se_tomou()
            if control2 == "2":

                print(mostra_remedio())
                input("aperte enter para continuar...")
        elif controle == "3":
            tomou()
        elif controle == "4":
            exclui_remedio()
        elif controle == "5":
            rodando = False


if __name__ == "__main__":
    rotina_inicial()
