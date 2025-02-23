#Melhore o jogo do desafio 028 onde o computador vai 'pensar' em um número entre 0 e 10. Só que ahora o jogador vai tentar adivinhar até acertar, mostrando no final quantos palpites foram nescessários para vencer.
from random import randint
from time import sleep
print('----------JOGO DA ADIVINHAÇÂO----------')
n = int(input('Escreva um número inteiro entre 0 e 10: '))

numEsc = randint(0,10)

print('PROCESSANDO...')
sleep(1)

c = 1
while n != numEsc:
    print('Você errou!')
    n = int(input('Escreva novamente um número inteiro entre 0 e 10: '))
    print('PROCESSANDO...')
    sleep(1)
    c += 1

print(f'Você acertou, o número escolhido foi {numEsc}')
print(f'Número de tentativas: {c}')
