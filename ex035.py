#Desenvolva um programa que leia o comprimeiro de três retas e diga ao usuário se elas podem ou não formar um triângulo.
r1 = float(input('Digite o valor da primeira reta: '))
r2 = float(input('Digite o valor da segunda reta: '))
r3 = float(input('Digite o valor da terceira reta: '))

if (r1 + r2) > r3 and (r1 + r3) > r2 and (r2 + r3) > r1:
    print(f'{r1} {r2} {r3}, formam um triângulo.')
else:
    print(f'{r1} {r2} {r3}, não formam um triângulo.')
