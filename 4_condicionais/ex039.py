#Faça um programa que leia o ano de nascimento de um jovem e informe, de acordo com sua idade: - Se ele ainda vai se alistar ao serviço militar. - Se é a hora de se alistar. - Se já passou do tempo do alistamento. Seu programa também deverá mostrar o tempo que falta ou que passou do prazo.
from datetime import date

print('-ALISTAMENTO MILITAR-')
sexo = str(input('Digite o seu sexo: M/F ')).upper()

if sexo == 'M':
    data = int(input('Digite o ano em que nasceu: '))

    idade = date.today().year - data

    if  idade == 18:
        print('Você deve se apresentar no alistamento obrigatório.')
    elif idade < 18:
        print(f'Ainda não é a hora de se alistar mas falta {18 - idade} anos para o alistamento.')
    else:
        print(f'Você já passou da hora de se alistar, já se passaram {idade - 18} anos desde o alistamento.')

elif sexo == 'F':
    print('Você não precisa fazer o serviço miltar obrigatório.')