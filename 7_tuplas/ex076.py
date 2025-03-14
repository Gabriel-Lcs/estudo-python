# Crie um programa que tenha uma tupla única com nomes de produtos e seus respectivos preços, na sequência. No final, mostre uma listagem de preços organizando os dados de forma tabular.
produtos = ('Lápis', 1.50, 'Caneta', 2.00, 'Caderno', 29.90, 'Lapiseria', 9.99, 'Borracha', 3.50, 'Livro', 34.90)

print('-' * 40)
print(f'{"PAPELARIA GAWEB":^40}')
print('-' * 40)

for i in range(0, len(produtos), 2):
    print(f'{produtos[i]:.<32}R${produtos[i + 1]:>6.2f}')
