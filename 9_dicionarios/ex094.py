# Crie um programa que leia nome, sexo e idade de várias pessoas, guardando os dados de cada pessoa em um dicionário e todos os dicionários em uma lista. No final mostre: A)Quantas pessoas foram cadastradas. B)A média de diade do grupo. C)Uma lista com todas as mulheres. D)Uma lista com todas as pessoas com idade acima da média.
grupo_pessoas = []
soma_idade = 0
contador = 1

while True:
    pessoa = {}
    print(f'Cadastrando a {contador}° pessoa'.center(45, '-'))
    pessoa['Nome'] = str(input('Nome: ')).capitalize()

    while True:
        sexo = str(input('Sexo [M/F]: ')).upper()
        if sexo in 'MF':
            break
        print('Erro! Digite apenas M ou F')
        
    pessoa['Sexo'] = sexo
    pessoa['Idade'] = int(input('Idade: '))
    
    grupo_pessoas.append(pessoa.copy())

    while True:
        resp = str(input('Deseja continuar? [S/N]: '))
        if resp in 'SsNn':
            break
        print('Erro! Digite apenas S ou N')

    if resp in 'Nn':
        break

    contador += 1

print('-' * 25)
print(f'- O grupo tem {len(grupo_pessoas)} pessoas.')

for i in grupo_pessoas:
    soma_idade += i['Idade']
media_idade = soma_idade/len(grupo_pessoas)
print(f'- A média de idade é de {media_idade} anos.')

print(f'- As mulheres cadastradas foram: ',end='')
for j in grupo_pessoas:
    if j['Sexo'] in 'F':
        print(j['Nome'], end='; ')

print(f'\n- Lista de pessoas com idade acimda da média: ')
for k in grupo_pessoas:
    if k['Idade'] > media_idade:
        for i, j in k.items():
            print(f'    {i} = {j};',end=' ')
        print()
