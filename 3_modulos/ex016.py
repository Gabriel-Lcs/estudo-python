#Crie um programa que leia um número real qualquer pelo teclado e mostre na tela sua porção inteira.
from math import trunc

n = float(input('Digite um número: '))

print(f'O número {n} tem a parte inteira {trunc(n)}.')
