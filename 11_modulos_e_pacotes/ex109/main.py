#Modifique as funções que foram criadas no desafio 107 para que elas acitem um parâmetro a mais, iformar se o valor retornado por elas vai ser ou não pela função moeda desenvolvida no desafio 108.
import moeda

valor = float(input('Digite o preço: R$'))

print(f'A metade de {moeda.cifrao(valor)} é {moeda.metade(valor, True)}')
print(f'O dobro de {moeda.cifrao(valor)} é {moeda.dobro(valor, True)}')
print(f'Aumentando 10% de {moeda.cifrao(valor)} é {moeda.aumentar(valor, 10, True)}')
print(f'Diminuindo 13% de {moeda.cifrao(valor)} é {moeda.diminiuir(valor, 13, True)}')
