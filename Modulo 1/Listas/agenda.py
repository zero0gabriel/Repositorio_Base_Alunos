from os import system


def limpa_tela():
    system("cls")


def adicionar_nome(lista_nomes, nome):
    lista_nomes.append(nome)


def remover_nome(lista_nomes, nome):
    if nome in lista_nomes:
        lista_nomes.remove(nome)
    else:
        print("Nome não encontrado!")


def mostrar_nomes(lista_nomes):
    for nome in lista_nomes:
        print(nome)


nomes = []

while True:
    limpa_tela()

    menu = input(
        "Escolha sua opção:\n"
        "[1] - Listar nomes\n"
        "[2] - Adicionar nomes\n"
        "[3] - Remover nomes\n"
        "[0] - Sair\n"
        "Sua opção: "
    )

    if menu == "0":
        break

    elif menu == "1":
        mostrar_nomes(nomes)
        input("Aperte Enter para continuar")

    elif menu == "2":
        nome_salvar = input("Digite o nome que deseja adicionar: ")
        adicionar_nome(nomes, nome_salvar)

    elif menu == "3":
        nome_remover = input("Digite o nome que deseja remover: ")
        remover_nome(nomes, nome_remover)