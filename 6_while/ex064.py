#Crie um programa que leia vários números inteiros pelo teclado. O programa só vai parar quando o usuário digitar o valor 999, que é a condição de parada. No final, mostre quantos número foram digitados e a soma entre eles(desconsiderando o flag).
n = 0
soma = 0 - 999
cont = 0 - 1

while n != 999:
    n = int(input('Digite um número: '))

    soma += n
    cont += 1

print(f'Foram digitados {cont} números e a soma entre eles é {soma}')
