def conjuntos_menu():
    opcao = int(input('\nCONJUNTOS\n\n1 - Verificar se A é subconjunto próprio de B\n2 - União de conjuntos\n3 - Intersecção de conjuntos\n4 - Diferença entre conjuntos\n5 - sair\n\n'))
    return opcao

def verificar_subconjunto():
    print('\nverificar')

def união_conjuntos():
    print('\nUnião')

def interseccao_conjuntos():
    print('\nIntersecção')

def diferenca_conjuntos():
    print('\nDiferença')

def init_conjuntos():
    while True:
        opcao = conjuntos_menu()
        if opcao == 1:
            verificar_subconjunto()
        elif opcao == 2:
            união_conjuntos()
        elif opcao == 3:
            interseccao_conjuntos()
        elif opcao == 4:
            diferenca_conjuntos()
        elif opcao == 5:
            print('\nVoltando pro menu...\n')
            break
        else:
            print('\nInválido')

