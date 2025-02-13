#Crie um programa que leia o ano de nascimento de sete pessoas. No final, mostre quatas pessoas ainda não atingiram a maioridade e quantas já são maiores.
from datetime import date

maioridade = 0
menoridade = 0

for i in range(0,7):
    ano_nasc = int(input('Digite a sua idade: '))

    idade = date.today().year - ano_nasc

    if idade >= 21:
        maioridade += 1
    else:
        menoridade += 1

print(f'No total tivemos {maioridade} pessoas maiores de idade e {menoridade} pessoas menores de idade.')
