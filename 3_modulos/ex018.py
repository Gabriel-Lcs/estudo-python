#Faça um programa que leia um ângulo qualquer e mostre na tela o valor do seno, cosseno e tangente desse ângulo.
from math import radians, sin, cos, tan
angulo = int(input("Digite um ângulo: "))

rad = radians(angulo)

print(f'O seno de {angulo} vale {sin(rad):.2f}')
print(f'O cosseno de {angulo} vale {cos(rad):.2f}')
print(f'O tangente de {angulo} vale {tan(rad):.2f}')
