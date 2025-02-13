#Desenvolva um programa que leia seis números inteiros e moestre a soma apenas daqueles que forem pares. Se o valor digitado for impar, desconsidere-o.
soma = 0

for i in range(0,6):
    n = int(input('Digite um número: '))
    if n % 2 == 0:
        soma += n

print(f'A soma é {soma}')
