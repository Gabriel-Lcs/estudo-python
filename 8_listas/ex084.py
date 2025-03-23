#Faça um programa que leia o nome e peso de várias pessoas, guardando tudo em uma lista. No final moestre: A)Quantas pessoas foram cadastradas. B)Uma listagem com as pessoas mais pesadas. C)Uma listagem com as pessoas mais leves.
pessoa = []
grupo = []

while True:
    pessoa.append(str(input('Nome: ')))
    pessoa.append(float(input('Peso: ')))
    grupo.append(pessoa[:])
    pessoa.clear()

    resp = str(input('Deseja continuar? [S/N] ')).upper()[0]

    if resp == 'N':
        break

for i in range(0, len(grupo)):
    if i == 0:
        maior = menor = grupo[i][1]
    else:
        if grupo[i][1] >= maior:
            maior = grupo[i][1]
        elif grupo[i][1] < menor:
            menor = grupo[i][1]

print('-' * 40)
print(f'Você cadastrou {len(grupo)} pessoas.')
print(f'O maior peso foi {maior:.1f}Kg. Peso de ', end='')
for j in range(0, len(grupo)):
    if grupo[j][1] == maior:
        print(grupo[j][0], end=' ')
        
print(f'\nO menor peso foi {menor:.1f}Kg. Peso de ', end='')
for k in range(0, len(grupo)):
    if grupo[k][1] == menor:
        print(grupo[k][0], end=' ')
