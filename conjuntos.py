def conjuntos_menu():
    opcao = input('\nCONJUNTOS\n\n1 - Verificar se A é subconjunto próprio de B\n2 - União de conjuntos\n3 - Intersecção de conjuntos\n4 - Diferença entre conjuntos\n5 - sair\n\n')
    return opcao

def verificar_subconjunto(A,B):
    print(30*'-')
    if set(A) != set(B) and set(A).issubset(set(B)):
        print("\nO conjunto A é subconjunto próprio de B\n")
    else:
        print("\nO conjunto A não é subconjunto próprio de B\n")


def união_conjuntos(A,B):
    print(30*'-')
    print(f'\nAUB = {set(A).union(set(B))}')

def interseccao_conjuntos(A,B):
    print(30*'-')
    print(f'\nIntersecção: {set(A).intersection(set(B))}\n')

def diferenca_conjuntos(A,B):
    print(30*'-')
    if len(set(A)) > len(set(B)):
        print(f'\nA - B = {set(A).difference(set(B))}\n')
    elif len(set(B)) > len(set(A)):
        print(f'\nB - A = {set(B).difference(set(A))}\n')
    else:
        print('{' + '}')


def criar_conjunto_A():
    conjA = set()
    print('\nmontando conjunto A...')
    while True:
        entrada = input('Insira um valor para adicionar ao conjunto A (deixe em branco para parar): ')
        if entrada == '':
            break
        num = int(entrada)
        conjA.add(num)
    return conjA

def criar_conjunto_B():
    conjB = set()
    print('\nmontando conjunto B...')
    while True:
        entrada = input('Insira um valor para adicionar ao conjunto B (deixe em branco para parar): ')
        if entrada == '':
            break
        num = int(entrada)
        conjB.add(num)
    return conjB


def init_conjuntos():
    conjA = criar_conjunto_A()
    conjB = criar_conjunto_B()
    while True:
        print(30*'-')
        print('\nConjunto A: ', conjA)
        print('Conjunto B: ', conjB)
        opcao = conjuntos_menu()
        if opcao == '1':
            verificar_subconjunto(conjA, conjB)
        elif opcao == '2':
            união_conjuntos(conjA, conjB)
        elif opcao == '3':
            interseccao_conjuntos(conjA, conjB)
        elif opcao == '4':
            diferenca_conjuntos(conjA, conjB)
        elif opcao == '5':
            print('\nVoltando pro menu...\n')
            break
        else:
            print('\nInválido')

