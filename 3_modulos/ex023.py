#Faça um programa que leia um número de 0 a 9999 e mostre na tela cada um dos digitos separados.
#---------COM STRING---------

# n = str(input('Digite um número de 0 a 9999: '))

# print(f'Unidade: {n[3]}')
# print(f'Dezena: {n[2]}')
# print(f'Centena: {n[1]}')
# print(f'Milhar: {n[0]}')

#--------MATEMATICA--------
n = int(input('Digite um número de 0 a 9999: '))

print(f'Unidade: {(n // 1) % 10}')
print(f'Dezena: {(n // 10) % 10}')
print(f'Centena: {(n // 100) % 10}')
print(f'Milhar: {(n // 1000) % 10}')
