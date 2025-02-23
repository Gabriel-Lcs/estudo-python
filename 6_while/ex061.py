#Refaça o desafio 051, lendo o primeiro termo e a razão de uma PA, mostrando os 10 primeiros termos da progressão usando estrutura while.
primeiro_termo = int(input('Digite o primeiro termo: '))
razao = int(input('Digite a razão: '))

cont = 1
while cont <= 10:
    print(f'{primeiro_termo}', end=' ')
    primeiro_termo += razao
    cont += 1
