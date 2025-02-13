#Faça um programa que leia três números e mostre qual o maior e qual é o menor.
n1 = int(input('Digite um número: '))
n2 = int(input('Digite um número: '))
n3 = int(input('Digite um número: '))

menor = n1
maior = n1

if n2 < menor:
    menor = n2
if n3 < menor:
    menor = n3

if n2 > maior:
    maior = n2
if n3 > maior:
    maior = n3

print(f'O menor é {menor}')
print(f'O maior é {maior}')
