from funcoes import *
import os 

while True:
    os.system("cls")
    match menu():
        case 1:
            cadastrar_cliente()
        case 2:
            cadastrar_filme()
        case 3:
            cadastrar_jogo()
        case 4:
            listar_itens()
        case 5:
            listar_clientes()
        case 6:
            alugar_item()
        case 7:
            devolver_item()
        case 0:
            print("Saindo...")
            break
        case _:
            print("Opção inválida!")
            os.system("pause")
