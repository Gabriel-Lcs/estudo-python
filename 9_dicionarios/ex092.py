#Crie um programa que leia nome, ano de nascimento e carteira de trabalho e cadastre-os(com idade) em um dicinário se for por acaso a CTPS for diferente de ZERO, o dicionário receberá também o ano de contribuição e o salário. Calcule e acrescente, além da idade, com quantos ans a pessoa vai se aposentar. Para se aposentar são 25 anos de contribuição.
from datetime import datetime
dados = {}

dados['Nome'] = str(input('Digite seu nome: ')).capitalize()
nascimento = int(input('Digite o ano de nascimento: '))
dados['Idade'] = datetime.today().year - nascimento
dados['CTPS'] = int(input('Carteira de Trabalho (0 se não tiver): '))

if dados['CTPS'] == 0:
    for i, j in dados.items():
        print(f'    - {i} tem o valor {j}')
else:
    dados['Contratação'] = int(input('Ano de contratação: '))
    dados['Salário'] = float(input('Salário R$: '))
    dados['Aponsetadoria'] =  (dados['Contratação'] - nascimento) + 35

    for i, j in dados.items():
            print(f'    - {i} tem o valor {j}')
