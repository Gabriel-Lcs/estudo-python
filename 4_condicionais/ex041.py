#A Confederação Nacional de Natação precisa de um programa que leia o ano de nascimento de um atleta e mostre sua categoria, de acordo com a idade: - Até 9 anos: MIRIM. - Até 14 anos: INFANTIL. - Até 19 anos: JUNIOR. - Até 25 anos: SÊNIOR. Acima: MASTER.
from datetime import date
print('-CONFEDERAÇÃO DE NATAÇÃO-')
ano = int(input('Digite o ano em que nasceu: '))

idade = date.today().year - ano

if idade <= 9:
    print('Sua categoria é MIRIM!')
elif idade > 9 and idade <= 14:
    print('Sua categoria é INFANTIL!')
elif idade > 14 and idade <= 19:
    print('Sua categoria é JUNIOR!')
elif idade > 19 and idade <= 25:
    print('Sua categoria é SÊNIOR!')
else:
    print('Sua categoria é MASTER!')
