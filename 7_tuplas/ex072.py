# Crie um programa que tenha uma tupla totalmente preenchida com uma contagem por extenso, de zero até vinte. Seu programa deverá ler um número pelo teclado (entre 0 e 20) e mostrá-lo por extenso.
while True:
    num = int(input('Digite um número entre 0 e 20: '))

    numeros = ('zero', 'um', 'dois', 'três', 'quatro', 'cinco', 'seis', 'sete', 'oito', 'nove', 'dez', 'onze', 'doze', 'treze', 'quatorze', 'quinze', 'dezesseis', 'dezessete', 'dezoito', 'dezenove', 'vinte')

    while num < 0 or num > 20:
        print('Número inválido!')
        num = int(input('Digite um número entre 0 e 20: '))

    print(f'Você digitou o número {numeros[num]}.')

    escolha = ' '
    while escolha not in 'SN':
        escolha = str(input('Deseja continuar? [S/N] ')).upper()
    
    if escolha == 'N':
        break
