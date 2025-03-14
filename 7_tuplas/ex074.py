# Crie um programa que vai gerar cinco números aleatórios e colocar em uma tupla. Depois disso, mostre a listagem de números gerados e também indique o menor e o maior valor que estão na tupla.
from random import randint
num = (randint(0, 10), randint(0, 10), randint(0, 10), randint(0, 10), randint(0, 10))

print('Os números sortiados foram', end=' ')
for i in num:
    print(i, end=' ')

print(f'\nO maior valor sorteado foi {max(num)}')
print(f'O menor valor sorteado foi {min(num)}')

maior = menor = num[0]

for i in range(0, len(num)):
    if num[i] > maior:
        maior = num[i]
    if num[i] < menor:
        menor = num[i]

print(f'O maior valor sorteado foi {maior}')
print(f'O menor valor sorteado foi {menor}')
