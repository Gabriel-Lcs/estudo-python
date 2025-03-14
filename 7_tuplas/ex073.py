# Crie uma tupla preenchida com os 20 primeiros colocados da Tabela do Campeonato Brasileiro de Futebol, na ordem de colocação. Depois mostre: A) Apenas os 5 primeiros colocados. B) Os últimos 4 colocados da tabela. C) Uma lista com os times em ordem alfabética. D) Em que posição da tabela está o time da Chapecoense.
times = ('Botafogo', 'Palmeiras', 'Flamengo', 'Fortaleza', 'Internacional', 'São Paulo', 'Corinthians', 'Bahia', 'Cruzeiro', 'Vasco', 'Vitória', 'Atlético-MG', 'Fluminense', 'Grêmio', 'Juventude', 'Red Bull Bragantino', 'Athletico-PR', 'Criciúma', 'Atlético-GO', 'Cuiabá')

print(f'Os 5 primeiros colocados são {" ".join(times[:5])}')
print('-' * 50)
print(f'Os 4 últimos colocados são {" ".join(times[-4:])}')
print('-' * 50)
print(f'A lista dos times em órdem alfabética fica: {" ".join(sorted(times))}')
print('-' * 50)

if 'Chapecoense' in times:
    print(f'O time da Chapecoense está na posição {times.index("Chapecoense") + 1} da tabela.')
else:
    print('Chapecoense não está no Brasileirão Série A 2024.')
    