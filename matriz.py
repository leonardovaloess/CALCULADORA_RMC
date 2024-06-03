def matrizes_menu():
    opcao = int(input('\nMATRIZES\n\n1 - Calcular determinante (Matrizes 2x2 e 3x3)\n2 - Multiplicação\n3 - Matriz transposta\n4 - Sair\n\n'))
    return opcao

def calcular_determinante(matriz ):
    #matriz = [
    #  [2, 3, 4], 2, 3
    #  [4, 3, 5], 4, 3
    #  [0, 2, 3], 0, 2
    #]
    if len(matriz) != len(matriz[0]):
        print('A matriz não é quadrada')
    elif len(matriz) == 2 and len(matriz[0]) == 2:
        determinante = matriz[0][0] * matriz [1][1] - matriz[0][1] * matriz[1][0]
        print(30*'-')
        print(f'\nDeterminante = {determinante}\n')
    elif len(matriz) == 3 and len(matriz[0]) == 3:
        #sofri aq professor 
        termo1 = matriz[0][0] * matriz[1][1] * matriz[2][2]
        termo2 = matriz[0][1] * matriz[1][2] * matriz[2][0]
        termo3 = matriz[0][2] * matriz[1][0] * matriz[2][1]
        termo4 = matriz[0][2] * matriz[1][1] * matriz[2][0]
        termo5 = matriz[0][1] * matriz[1][0] * matriz[2][2]
        termo6 = matriz[0][0] * matriz[1][2] * matriz[2][1]
        determinante = termo1 + termo2 + termo3 - termo4 - termo5 - termo6

        print(30*'-')
        print(f'\nDeterminante = {determinante}\n')
        
    

def montar_matriz():
    numLinhas = int(input('Insira o numero de linhas: '))
    numColunas = int(input('Insira o numero de colunas: '))
    matriz = []
    for i in range(numLinhas):
        linha = []
        for j in range(numColunas):
            num = int(input(f'Insira o valor do elemento a[{i}][{j}]'))
            linha.append(num)
        matriz.append(linha)
    
    return matriz
    

def multiplicação(matriz):
    print(30*'-')
    print('\nCriando segunda matriz\n')
    matriz2 = montar_matriz()
    
    if len(matriz[0]) == len(matriz2):
        matriz_resultante = [[0 for _ in range(len(matriz2[0]))] for _ in range(len(matriz))]
        print('\n')
        print_matriz(matriz)
        print('\nx\n')
        print_matriz(matriz2)
        for i in range(len(matriz)):
            for j in range(len(matriz2[0])):
                for k in range(len(matriz2)):
                    matriz_resultante[i][j] += matriz[i][k] * matriz2[k][j]
        print('\n=\n')
        print_matriz(matriz_resultante)
        print('\n', 30 * '-')
        
    else:
        print('\nAs matrizes não satisfazem a condição de multiplicação (a[j] != b[i])\n')
        print(30*'-')
        
    
    
def transposta(matriz):
    print(30*'-')
    transposta = []
    for i in range(len(matriz[0])):
        linha = []
        for j in range(len(matriz)):
            linha.append(matriz[j][i])
        transposta.append(linha)
    print('\ntransposta:\n')
    print_matriz(transposta)
    print('\n',30*'-')
    

def print_matriz(matriz):
    for linha in matriz:
        print(linha)

def init_matrizes():
    matriz = montar_matriz()
    print('\n')
    print_matriz(matriz)
    while True:
        opcao = matrizes_menu()
        if opcao == 1:
            calcular_determinante(matriz)
            print(30*'-')
        elif opcao == 2:
            multiplicação(matriz)
        elif opcao == 3:
            transposta(matriz)
        elif opcao == 4:
            print('\nVoltando pro menu...\n')
            break
        else:
            print('\nInválido')

init_matrizes()