#Crie um programa onde 4 jogadores joguem um dado e tenham resultados aleatórios. Guarde esses resultados em um dicionário. No final, coloque esse dicionário um ordem sabendo que o vencedor tirou o maior número no dado.
from random import randint
jogadores = {}

for i in range(1, 5):
    jogadores[f'Jogador {i}'] = randint(1,6)
    
for j, k in jogadores.items():
    print(f'O {j} tirou: {k}')
    
ranking = sorted(jogadores, key = jogadores.get, reverse = True)

for c, i in enumerate(ranking):
    print(f'{c + 1}° Lugar: {i} com {jogadores[i]} ')
