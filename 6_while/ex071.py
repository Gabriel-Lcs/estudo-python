#Crie um programa que simule o funcionamento de um caixa eletrônico. No início, pergunte ao usuário qual será o valor a ser sacado (número inteiro) e o programa vai informar quantas cédulas de cada valor serão entegues. OBS: Considere que o caixa possui céudas de R$50, R$20, R$10 e R$1
print('-' * 15)
print(f'{"Banco Gaweb":^15}')
print('-' * 15)

cinquenta = 0
vinte = 0
dez = 0
um = 0

valor = int(input('Qual valor deseja sacar? R$'))

while True:
    if valor == 0:
        print('Fim do programa')
        
        if cinquenta >= 1:
            print(f'{cinquenta} notas de R$50.')
        if vinte >= 1:
            print(f'{vinte} notas de R$20.')
        if dez >= 1:
            print(f'{dez} notas de R$10.')
        if um >= 1:
            print(f'{um} notas de R$1.')

        break

    while valor >= 50:
        valor -= 50
        cinquenta += 1
        
    while valor >= 20:
        valor -= 20
        vinte += 1

    while valor >= 10:
        valor -= 10
        dez += 1
          
    while valor >= 1:
        valor -= 1
        um += 1
