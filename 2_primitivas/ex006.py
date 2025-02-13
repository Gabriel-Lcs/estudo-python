#Crie um algorítmo que leia um número e mostre o seu dobro, triplo e raiz quadrada.
from math import sqrt
n = int(input('Digite um número: '))

print(f'O dobro de {n} é {n * 2}, o seu triplo é {n * 3} e sua raiz quadrada é {sqrt(n):.2f}')
