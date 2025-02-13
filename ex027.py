#Faça um programa que leia o nome completo de uma pessoa, mostrando em seguida o primeiro e o ultimo nome separadamente.
n = str(input('Digite o seu nome: ')).title().split()

print(f'Primeiro nome: {n[0]}')
print(f'Ultimo nome: {n[-1]}')
