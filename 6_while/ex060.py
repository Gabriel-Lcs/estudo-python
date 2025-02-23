#Faça um programa que leia um número qualquer e mostre seu fatorial.
n = int(input('Digite um número: '))

fat = 1
contador = 1
while contador != (n + 1):
    fat *= contador
    contador += 1

print(f'o fatorial de {n} é {fat}')
