#Crie um programa que tenha uma função fatorial() que receba dois parâmetros: o primeiro que indique o número a calcular e outro chamado show, que será um valor lógico(opcional) indicando se será mostrado ou não na tela o processo de cálculo do fatorial.
def fatorial(num = 1, show = False):
    """
    -> Função que calcula o fatorial de um número.
        :parâmetro num: é o número que vai ser calclulado
        :parâmetro show: é um parâmetro opcional para mostrar ou não a conta
        :return: o valor do fatorial de um número n
    """
    fat = 1
    for i in range(num, 0, -1):
        fat *= i

    if show == True:
        for i in range(num, 1, -1):
            print(i, end=' x ')
            
        print('1 = ', end='')

    return fat


print(fatorial(10, True))
