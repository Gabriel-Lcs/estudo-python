#Faça um programa que jogue par ou ímpar com o computador. O jogo só será interrompido quando o jogador perder, mostra o total de vitórias consecutivas que ele conquistou no final do jogo.
from random import randint
consec = 0

while True:
    pc = randint(0,10)

    print('VAMOS JOGAR PAR OU ÍMPAR')
    valor = int(input('Digite um valor: '))

    reslt = valor + pc

    par_impar = str(input('Par ou Ímpar [P/I]? ')).strip().upper()
    while par_impar not in 'PI':
        par_impar = str(input('Par ou Ímpar [P/I]? ')).strip().upper()

    if par_impar == 'P':
        if reslt % 2 == 0:
            print(f'Sua escolha foi {valor} e o computador escolheu {pc}.O total é {valor + pc} por isso é par.Você ganhou!')
            consec += 1

        else:
            print(f'Sua escolha foi {valor} e o computador escolheu {pc} a soma é {valor + pc} por isso é ímpar.Você Perdeu!')
            break

    elif par_impar == 'I':
        if reslt % 2 != 0:
            print(f'Sua escolha foi {valor} e o computador escolheu {pc} a soma é {valor + pc} por isso é ímpar.Você ganhou!')
            consec += 1

        else:
            print(f'Sua escolha foi {valor} e o computador escolheu {pc} a soma é {valor + pc} por isso é par.Você Perdeu!')
            break
    
    else:
        print('Opção inválida.')

print(f'Você ganhou {consec} vezes consecutivas.')
