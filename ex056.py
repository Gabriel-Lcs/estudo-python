#Desenvolva um programa que leia o nome, idade e sexo de 4 pessoas. No final do programa, mostre: - A média de idade do grupo. - Qual o nome do homem mais velho. - Qauntas mulheres tem menos de 20 anos.
soma_idade = 0
homem_velho = ""
idade_homem = 0
qnt_mulheres_21_anos = 0

for i in range (0,4):
    print(f'{" Cadastre uma nova pessoa ":=^50}')
    nome = str(input('Digite seu nome: '))
    idade = int(input('Digite sua idade: '))
    sexo = str(input('Digite seu sexo: Mm/Ff ')).upper()

    soma_idade += idade
    media_idade = soma_idade / 4

    if sexo == "M":
        if idade > idade_homem:
            idade_homem = idade
            homem_velho = nome
    elif sexo == "F":
        if idade < 20:
            qnt_mulheres_21_anos += 1

print(f'A média de idade do grupo é {media_idade} anos.')
print(f'O nome do homem mais velho é {homem_velho}.')
print(f'Tem um total de {qnt_mulheres_21_anos} mulheres com menos de 20 anos.')
