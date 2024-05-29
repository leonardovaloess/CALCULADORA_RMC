import math
import cmath
def func2grau_menu():
    opcao = input('\nFUNÇÕES DO SEGUNDO GRAU\n\n1 - Calcular raízes\n2 - Calcular função em x pedido (f(x) = resultado)\n3 - Calcular vértice\n4 - Gerar gráfico\n5 - sair\n\n')
    return opcao


def calc_raizes(a, b, c):
    print(30*'-')
    delta = b**2 - 4*a*c
    if delta > 0:
        x1 = (-b + math.sqrt(delta))/(2*a)
        x2 = (-b - math.sqrt(delta))/(2*a)
        print(f'\nRaízes: x1 = {x1} , x2 = {x2}\n')
    elif delta < 0:
        delta_complexo = cmath.sqrt(delta)
        x1 = (-b + delta_complexo)/(2*a)
        x2 = (-b - delta_complexo)/(2*a)
        print(f'\nRaízes complexas: x1 = {x1} , x2 = {x2}\n')
    elif delta == 0:
        x = -b/(2*a)
        print(f'\nx = {x}\n')



def calcular_funcao(a,b,c):
    print(30*'-')
    x = int(input('Insira o valor de x: '))
    fx = (a*(x**2)) + (b * x) + c
    print(f'\nf({x}) = {fx}\n')




def calcular_vertice(a,b,c):
    print(30*'-')
    delta = b**2 - 4*a*c
    Yv = -delta/(4*a)
    Xv = -b/(2*a)
    print(f'\nYv = {Yv}\nXv = {Xv}\n')

#def mostrar_grafico(a,b,c):
#    print(30 * '-')
#    def quadratic_function(x):
#        return a * x**2 + b * x + c
#    
#    # Gerar pontos para o gráfico
#    x = np.linspace(-10, 10, 400)
#    y = quadratic_function(x)
#    
#    # Criar o gráfico
#    plt.figure(figsize=(8, 6))
#    plt.plot(x, y, label=f'f(x) = {a}x² + {b}x + {c}')
#    plt.title('Gráfico de uma função quadrática')
#    plt.xlabel('x')
#    plt.ylabel('f(x)')
#    plt.grid(True)
#    plt.legend()
#    plt.show()
#    print('\nDiferença')

def init_2grau():
    a = int(input('\nInsira o valor de a: '))
    b = int(input('\nInsira o valor de b: '))
    c = int(input('\nInsira o valor de c: '))
    while True:
        print(30*'-')
        print(f'\nf(x) = {a}x² + {b}x + {c}')
        opcao = func2grau_menu()
        if opcao == '1':
            calc_raizes(a, b, c)
        elif opcao == '2':
            calcular_funcao(a,b,c)
        elif opcao == '3':
            calcular_vertice(a,b,c)
        elif opcao == '4':
            #mostrar_grafico()
            print('\nGráfico\n')
        elif opcao == '5':
            print('\nVoltando pro menu...\n')
            break
        else:
            print('\nInválido')

