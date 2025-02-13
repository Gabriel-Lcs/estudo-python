#Escreva um programa que faça o computador "pensar" em um número inteiro entre 0 e 5 e peça para o usuário tentar descobrir qual foi o número esscolhido pelo computador.
from random import randint
from time import sleep
print('----------JOGO DA ADIVINHAÇÂO----------')
n = int(input('Escreva um número inteiro entre 0 e 5: '))

numEsc = randint(0,5)

print('PROCESSANDO...')
sleep(2)

if n == numEsc:
    print(f'PARABÉNS, você acertou o número escolhido!')
else:  
    print(f'Você errou! O número escolhido era {numEsc}')
