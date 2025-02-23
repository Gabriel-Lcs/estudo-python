#Crie um programa que leia dois valores e mostre um menu na tela: [1] - Somar [2] - Multiplicar [3] - Maior [4] - Novos números [5] - Sair do programa. Seu programa deverá realizar a operação solicitada.
n1 = int(input('Digite o primeiro número: '))
n2 = int(input('Digite o segundo número: '))

opcao = 0
while opcao != 5:
    print('''    [1] - Somar
    [2] - Multiplicar
    [3] - Maior
    [4] - Novos números
    [5] - Sair do programa ''')

    opcao = int(input('Escolha sua opção: '))

    if opcao == 1:
        print(f'A soma entre {n1} + {n2} é {n1+n2}')
    elif opcao == 2:
        print(f'A Multiplicação entre {n1} x {n2} é {n1*n2}')
    elif opcao == 3:
        if n1 > n2:
            maior = n1
        else:
            maior = n2

        print(f'O maior número entre {n1} e {n2} é {maior}')
    elif opcao == 4:
        n1 = int(input('Digite o primeiro número: '))
        n2 = int(input('Digite o segundo número: '))
    elif opcao == 5:
        print('Programa finalizado')
    else:
        print('Opção inválida, digite novamente!')
