#Crie um programa que leia o nome e preço de vários produtos. O programa deverá perguntar se o usuário vai continuar. No final, mostre: A) Qual é o total gasto na compra. B) Quantos produtos custam mais de R$1000,00. C) Qual é o nome do produto mais barato.
soma = 0
mais_mil = 0
nome_produto_barato = ''
preco_produto_barato = 0

while True:
    print('-' * 15)
    print(f'{"LOJINHA":^15}')
    print('-' * 15)

    produto = str(input('Nome do produto: '))
    preco = float(input('Preço do produto: R$'))
    continuar = str(input('Deseja continuar [S/N]? ')).strip().upper()
    while continuar not in 'SN':   
        continuar = str(input('Deseja continuar [S/N]? ')).strip().upper()
    
    soma += preco
    if preco > 1000:
        mais_mil += 1

    if preco_produto_barato == 0 or preco < preco_produto_barato:
        preco_produto_barato = preco
        nome_produto_barato = produto
        
    if continuar == 'N':
        print('FIM DO PROGRAMA')
        print(f'O total da compra foi R${soma:.2f}')
        print(f'{mais_mil} produtos custando mais de R$1000.00')
        print(f'O produto mais barato foi {nome_produto_barato} que custa R${preco_produto_barato:.2f}')
