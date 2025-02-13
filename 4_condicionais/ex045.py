#Crie um programa que faça o computador jogar Pedra, papel e tesoura com você.
from random import choice
from time import sleep

esc = str(input('Escolha pedra, papel ou tesoura: ')).upper()

escPc = choice(['Pedra', 'Papel', 'Tesoura'])

sleep(2)
print(f'O computador escolheu {escPc}.')

if escPc == 'Pedra' and esc == 'PEDRA':
    print('EMPATE!')
elif escPc == 'Pedra' and esc == 'PAPEL':
    print('VOCÊ GANHOU, PARABÉNS!')
elif escPc == 'Pedra' and esc == 'TESOURA':
    print('O COMPUTADOR GANHOU, QUE PENA.')
elif escPc == 'Papel' and esc == 'PEDRA':
    print('O COMPUTADOR GANHOU, QUE PENA.')
elif escPc == 'Papel' and esc == 'PAPEL':
    print('EMPATE!')
elif escPc == 'Papel' and esc == 'TESOURA':
    print('VOCÊ GANHOU, PARABÉNS!')
elif escPc == 'Tesoura' and esc == 'PEDRA':
    print('VOCÊ GANHOU, PARABÉNS!')
elif escPc == 'Tesoura' and esc == 'PAPEL':
    print('O COMPUTADOR GANHOU, QUE PENA.')
elif escPc == 'Tesoura' and esc == 'TESOURA':
    print('EMPATE!')
