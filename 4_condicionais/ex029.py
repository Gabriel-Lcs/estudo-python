#Escreva um programa que leia a velocidade de um carro. Se ele ultrapassar 80Km/h, mostre uma mensagem dizendo que ele foi multado. A multa vai custar R$7 por cada Km acima do limite.
velocidade = int(input('Digite a velocidade em que o carro estava: Km/h '))

multa = 7 * (velocidade - 80)

if velocidade > 80:
    print(f'O carro foi multado! A multa foi no valor de R${multa}')
else:
    print('O carro está em uma velocidade boa.')
