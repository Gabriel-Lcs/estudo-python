#Faça um programa que calcule a soma entre todos os números ímpares que esão múltiplos de três e que se encontram no intervalo de 1 até 500.
soma = 0

for i in range(1, 501, 2):
    if i % 3 == 0:
        soma += i

print(f'A soma é {soma}')
