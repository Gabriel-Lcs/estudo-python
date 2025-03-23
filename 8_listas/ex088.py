#Faça um programa que ajude um jogador da MEGA SENA a criar palpites. O programa vai perguntar quantos jogos serão gerados e vai sortear 6 números entre 1 e 60 para cada jogo cadastrando tudo em uma lista composta.
from random import randint
from time import sleep
total = []
jogos = []

print('-' * 30)
print(f'{"MEGA SENA":^30}')
print('-' * 30)

n = int(input('Quantos jogos você quer jogar? '))

for i in range(0, n):
    c = 0

    while c < 6:
        sorteado = randint(1,60)

        if sorteado not in jogos:
            jogos.append(sorteado)
            c += 1

    total.append(jogos[:])
    jogos.clear()

    sleep(1)
    print(f'Jogo {i+1}: {sorted(total[i])}')
