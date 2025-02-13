#Escreva um programa para aprovar o empréstimo bancário para a compra de uma casa. O programa vai perguntar o valor da casa, o salário do comprador e em quantos anos ele vai pagar. Calcule o valor da prestação mensal, sabendo que ela não pode exceder 30% do salário ou então o empréstimo será negado.
valor = float(input('Qual o valor da casa? R$'))
salario = float(input('Qual o seu salário? R$'))
anos = int(input('Em quantos anos pretende pagar a casa? '))

prest = valor / (anos * 12)

if prest > (salario * 0.3):
    print(f'Para comprar uma casa de R${valor:.2f} em {anos} anos a prestação será de R${prest:.2f} e seu salário é muito pouco, por isso empretimo NEGADO!')
else:
    print(f'Uma casa com o valor de R${valor:.2f} que vai ser pagar em {anos} anos vai ser com uma mensalidade de R${prest:.2f}, empréstimo CONCEDIDO!')
