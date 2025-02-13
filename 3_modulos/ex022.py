#Crie um programa que leia o nome completo de uma pessoa e mostre: -O nome com todas as letras maiúsculas; -O nome com todas minúsculas; -Quantas letras ao todo(sem considerar espaços); -Quantas letras tem o primeiro nome.
nome = str(input('Digite seu nome completo: ')).strip()

print(f'Maiúsculas: {nome.upper()}')
print(f'Minúsculas: {nome.lower()}')
print(f'Quantas letras no total: {len(nome) - nome.count(" ")}')
print(f'Quantas letras no primeiro nome: {len(nome.split()[0])}')
