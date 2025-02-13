#Escreva um progrmaa que leia um número inteiro qualquer e peça para o usuário escolher a base de converão: - 1 para binário. - 2 para octal. - 3 para hexadecimal.
n = int(input('Digite um número: '))
print(
'''
[1] - BINÁRIO
[2] - OCTAL
[3] - HEXADECIMAL
''')
esc = int(input('Escolha a transformação: '))
if esc == 1:
    print(f'O valor em binário de {n} é: {bin(n)[2:]}')
elif esc == 2:
    print(f'O valor em octal de {n} é: {oct(n)[2:]}')
elif esc == 3:
    print(f'O valor em hexadecimal de {n} é: {hex(n)[2:]}')
