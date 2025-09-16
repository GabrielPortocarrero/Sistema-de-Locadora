from classes import *

def menu()
    print("---BEM VINDO A LOCADORA---")
    print("1 - CADASTRAR CLIENTE")
    print("2 - CADASTRAR FILME")
    print("3 - CADASTRAR JOGO")
    print("4 - LISTAR ITENS")
    print("5 - LISTAR CLIENTE")
    print("6 - ALUGAR ITEM")
    print("7 - DEVOLVER ITEM")
    print("0 - SAIR")
    escolha = int(input("-->"))
    return escolha

def cadastrar_cliente():
    os.system("cls")
    nome = input("Informe seu nome:")
    cpf = input("Informe seu CPF:")
    novo_cliente = Clientes(nome, cpf)

    def cadastrar_item():
        os.system("cls")
        titulo = input("Informe o titulo do item:")
        tipo = int(input("Informe o tipo do item (1 - Filme / 2 - Jogo):"))
    if tipo == 1:
        genero = input("Informe o genero do filme:")
        duracao = input("Informe a duracao do filme:")
        novo_cliente = Filme(titulo, genero, duracao)
    elif tipo == 2:
        plataforma = input("Informe a plataforma do jogo:")
        faixa_etaria = input("Informe a faixa etaria do jogo:")
        novo_cliente = Jogo(titulo, plataforma, faixa_etaria)

        def listar_itens():
            os.system("cls")
            print("-----LISTA DE ITENS-----")
        for item in Locadora.items:
            status = "Disponivel" if item.disponivel else "Indisponivel"
            print(f"Código: {item.codigo} / Titulo: {item.titulo} / Status: {status}")
            input("Pressione ENTER para continuar...")
