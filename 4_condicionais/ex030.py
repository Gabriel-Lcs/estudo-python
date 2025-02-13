#Crie um progama que leia um número inteiro e mostre na tela se ele é impar ou par.
n = int(input('Digite um número: '))

if n % 2 == 0:
    print(f'{n} é par.')
else:
    print(f'{n} é impar.')
