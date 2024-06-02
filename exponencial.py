import numpy as np
import matplotlib.pyplot as plt

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

def gerar_grafico(a, b):
    print(30 * '-')
    x = np.linspace(-10, 10, 400)  # Intervalo de x de -10 a 10
    y = a**x + b
    
    plt.figure(figsize=(8, 6))
    plt.plot(x, y, label=f'f(x) = {a}^x + {b}')
    
    plt.axhline(0, color='black',linewidth=0.5)
    plt.axvline(0, color='black',linewidth=0.5)
    plt.grid(color='gray', linestyle='--', linewidth=0.5)
    plt.legend()
    plt.title('Gráfico da Função Exponencial')
    plt.xlabel('x')
    plt.ylabel('f(x)')
    plt.show()

def init_exponencial():
    global a
    global b
    while True:
        a = float(input('Insira o valor de a: '))
        if a == 0 or a == 1 or a < 0:
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
            gerar_grafico(a,b)
        elif opcao == '4':
            print('\nVoltando pro menu...\n')
            break
        else:
            print('\nInválido')

