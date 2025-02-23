#Crie um programa que leia vários números inteiros pelo teclado. O programa só vai parar quando o usuário digitar o valor 999, que é a condição de parada. No final, mostre quantos número foram digitados e a soma entre eles(desconsiderando o flag).
soma = 0
c = 0
while True:
    n = int(input('Digite um valor (999 para parar): '))

    if n == 999:
        break

    soma += n
    c += 1

print(f'Foi digitado {c} números e sua soma é {soma}.')
