#Crie um programa que gerencie o aproveitamento de um jogador de futebol. O programa vai ler o nome do jogador e quantas partidas ele jogou. Depois vai ler a quantidade de gols feitos em cada partida. No final, tudo isso será guardado em um dicionário, incluindo o total de gols feitos durante o cameonato.
jogador = {}
gols = []
soma_gols = 0
jogador['nome'] = str(input('Nome do jogador: ')).capitalize()
partidas = int(input('Quantas partidas ele jogou? '))

for i in range(0, partidas):
    gols.append(int(input(f'Quantos gols na partida {i + 1}? ')))
jogador['gols'] = gols

for i in gols:
    soma_gols += i
jogador['total'] = soma_gols

print('-' * 40)
print(jogador)
print('-' * 40)

for l, m in jogador.items():
    print(f'O campo {l} tem o valor {m}.')
print('-' * 40)

print(f'O jogador {jogador["nome"]} jogou {partidas} partidas.')
for c, i in enumerate(jogador['gols']):
    print(f'    -> Na partida {c + 1}, fez {i} gols')
    
print(f'Fez um total de {jogador["total"]} gols.')
