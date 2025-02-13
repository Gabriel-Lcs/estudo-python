#Crie um progama que leia quanto de dinheiro uma pessoa tem na carteira e mostre quantos dólares ela pode comprar. Considere US$ = R$6.17
n = float(input('Quanto você tem na carteira? R$'))

print(f'Com R${n:.2f} é possível comprar US${n / 6.17:.2f}')
