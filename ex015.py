#Escreva um programa que pergunte a quantidade de Km percorridos por um carro alugado e a quantidade de dias pelos quais ele foi alugado. Calcule o preço a apagar, sabendo que o carro custa R$60 por dia e R$0,15 por Km rodado.
dias = int(input('Quantos dias o carro foi alugado? '))
km = float(input('Quantos Km foram rodados no carro? '))

preco = (60 * dias) + (km * 0.15)

print(f'Com o carro sendo alugado por {dias} dias e rodado {km}Km o preço total do aluguel foi {preco:.2f} reais.')
