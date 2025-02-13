#Faça um programa que leia um número inteiro e diga se ele é ou não um número primo.
n = int(input('Digite um número: '))

contagem = 0

for i in range(1, n+1):
    if n % i == 0:
        contagem += 1
        
if contagem == 2:
    print(f'{n} é primo.')
else:
    print(f'{n} não é primo.')
