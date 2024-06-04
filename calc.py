import conjuntos
import f2grau
import exponencial
import matriz


def menu():
    opcao = input('\nMENU:\n\n1 - Conjunto numéricos\n2 - Funções do segundo grau\n3 - Funções exponenciais\n4 - Matrizes\n5 - Sair\n\n')
    return opcao 

def init():
    while True:
        opcao = menu()
        if opcao == '1':
            print(30*'-')
            conjuntos.init_conjuntos()
            print(30*'-')
        elif opcao == '2':
            print(30*'-')
            f2grau.init_2grau()
            print(30*'-')
        elif opcao == '3':
            print(30*'-')
            exponencial.init_exponencial()
            print(30*'-')
        elif opcao == '4':
            matriz.init_matrizes()
        elif opcao == '5':
            print('\nSaindo...')
            break
        else:
            print('\nInválido')

init()