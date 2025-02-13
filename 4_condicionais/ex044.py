#Elabore um programa que calcule o valor a ser pago por um produto, considerando o seu preço normal e condição de pagamento: - À vista dinheiro/cheque: 10% de desconto. - À vista no cartão: 5% de desconto. - Em até 2x no cartão: Preço normal. - 3x no cartão: 20% de juros.
preco = float(input('Digite o valor total da compra: R$'))
print("""
**********ESCOLHA SUA CONDIÇÃO DE PAGAMENTO**********
[1] - À vista dinheiro/cheque.
[2] - À vista no cartão.
[3] - Em até 2x no cartão.
[4] - 3x ou mais no cartão.
""")
esc = int(input('Escolha seu pagamento: '))

if esc == 1:
    print(f'Sua compra de R${preco:.2f} recebeu um desconto de 10% e ficará R${preco * 0.9:.2f}')
elif esc == 2:
    print(f'Sua compra de R${preco:.2f} recebeu um desconto de 5% e ficará R${preco * 0.95:.2f}')
elif esc == 3:
    print(f'Sua compra de R${preco:.2f} ficará os mesmos R${preco:.2f}')
elif esc == 4:
    parcela = int(input('Em quantas parcelas? '))
    print(f'Sua compra de R${preco:.2f} recebeu um acréssimo de 20% e ficará R${preco * 1.2:.2f}')
    print(f'Sua parcela em {parcela}x vai ficar R${(preco * 1.2)/parcela:.2f}')
else:
    print('OPÇÃO INVÁLIDA!')
