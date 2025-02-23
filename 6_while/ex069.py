#Crie um programa que leia a idade e o sexo de várias pessoas. A cada pessoa cadastrada, o progama deverá perguntar se o usuário quer ou não continuar. No final, mostre: A) Quantas pessoas tem mais de 18 anos. B)Quantos homens foram cadastrados. C)Quantas mulheres tem menos de 20 anos.
mais_18 = 0
cont_h = 0
mulher20 = 0

while True:
    print('-' * 20)
    print('Cadastre uma pessoa')
    print('-' * 20)

    idade = int(input('Idade: '))

    sexo = str(input('Sexo [M/F]: ')).strip().upper()
    while sexo not in 'MF':
        sexo = str(input('Sexo [M/F]: ')).strip().upper()

    continuar = str(input('Deseja continuar [S/N]? ')).strip().upper()
    while continuar not in 'SN':
        continuar = str(input('Deseja continuar [S/N]? ')).strip().upper()

    if idade >= 18:
        mais_18 += 1
    if sexo == 'M':
        cont_h += 1
    if sexo == 'F' and idade < 20:
        mulher20 += 1

    if continuar == 'N':
        print('------- FIM DO PROGRAMA -------')
        print(f'Há {mais_18} pessoas com mais de 18 anos.')
        print(f'Foram cadastrados {cont_h} homens.')
        print(f'Há {mulher20} mulheres com menos de 20 anos.')
        break
