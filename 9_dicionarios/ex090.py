#Faça um programa que leia noeme média de um aluno, guardando também a situação em um dicionário. No final, mostre o conteúdo da estrutura na tela.
aluno = {}

aluno['Nome'] = str(input('Digite o nome do aluno: '))
media = float(input(f'Digite a média de {aluno["Nome"]}: '))
aluno['Média'] = media

if media > 7:
    aluno['Situação'] = 'Aprovado'
else:
    aluno['Situação'] = 'Reprovado'

for i, j in aluno.items():
    print(f'    - {i} é igual a {j}')
