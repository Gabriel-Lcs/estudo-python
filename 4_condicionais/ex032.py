#Faça um programao que leia um ano qualquer e mostre se ele é bissexto.
from datetime import date
ano = int(input('Que ano quer analizar? Digite 0 para analizar o ano atual em que está: '))

if ano == 0:
    ano = date.today().year

if ano % 4 == 0 and ano % 100 == 0 or ano % 400 == 0:
    print(f'{ano} é bissexto')
else:
    print(f'{ano} não é bissexto')
