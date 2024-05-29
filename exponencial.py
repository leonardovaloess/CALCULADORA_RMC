def exponencial_menu():
    opcao = input('\nFUNÇÃO EXPONENCIAL\n\n1 - Verificar se é crescente ou decrescente\n2 - Calcular função em x pedido (f(x) = resultado)\n3 - Gerar gráfico\n4 - sair\n\n')
    return opcao

def verificar_crescente(a):
    print(30*'-')
    if a > 1:
        print('É crescente')
    else: 
        print('É decrescente')
        
        
def calcular_func(a,b):
    print(30*'-')
    x = int(input('Insira o valor de x: '))
    fx = (a**x) + b
    print(f'f({x}) = {fx}')

def gerar_grafico():
    print('gráfico')

def init_exponencial():
    global a
    global b
    while True:
        a = int(input('Insira o valor de a: '))
        if a == 0 or a == 1:
            print('O valor de A não respeita a condição de existencia')
        else:
            b = int(input('insira o valor de b: '))
            break
            
    while True:
        print(30*'-')
        print(f'f(x) = {a}**x + {b}')
        opcao = exponencial_menu()
        if opcao == '1':
            verificar_crescente(a)
        elif opcao == '2':
            calcular_func(a,b)
        elif opcao == '3':
            gerar_grafico()
        elif opcao == '4':
            print('\nVoltando pro menu...\n')
            break
        else:
            print('\nInválido')

