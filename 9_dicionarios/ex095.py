#Aprimore o DESAFIO 093 para que ele funcione com vários jogadores, incluidno um sistema de visualização de detalhes do aproveitamento de cada jogador.
jogadores = []

while True:
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

    jogadores.append(jogador.copy())

    while True:
        resp = str(input('Deseja contirnuar? [S/N] ')).upper()[0]
        if resp in 'SN':
            break

        print('Erro! Digite apenas S ou N')

    if resp == 'N':
        break
    print('-' * 40)

print('-=' * 20)

print(f'{"Cod":<4}{"Nome":<15}{"Gols":<15}{"Total":<4}')
print('-' * 40)

for c, i in enumerate(jogadores):
    print(f'{c:<4}{i["nome"]:<15}{str(i["gols"]):<15}{i["total"]:<4}')

print('-=' * 20)

while True:
    esc = int(input('Mostrar dados de qual jogador? (999 para sair) '))

    if esc > len(jogadores) - 1:
        if esc == 999:
            break
        print(f'Erro! Não esxite jogador com código {esc}, tente novamente!')
        print('-' * 40)
    else:
        print(f'-> LEVANTAMENTO DO JOGADOR: {jogadores[esc]["nome"]}')

        for c, i in enumerate(jogadores[esc]['gols']):
            print(f'    No jogo {c + 1} fez {i}')

print('Programa finalizado.')
