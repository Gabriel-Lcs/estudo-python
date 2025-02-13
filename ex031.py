#Desenvolva um programa que pergunte a distância de uma viagem em Km. Calcule o preõ da passagem, cobrando R$0,50 por Km para viagens até 200Km e R$0,45 para viagens mais longas.
distancia = float(input('Digite a distância da viagem: '))

if distancia >= 200:
    preco = distancia * 0.45
else:
    preco = distancia * 0.5

print(f'O valor para a distância de {distancia} Km é R${preco:.2f}')
