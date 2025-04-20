#Crie um pacote chamado utilidadeCeV que tenha doi s módulos internos chamado moeda e dado. Transfira todas as funções utilizadas nos desafios 107, 108 e 109 para o primeiro pacote e mantenha tudo funcionando.
from utilidadeCeV import moeda

valor = float(input('Digite o preço: R$'))
moeda.resumo(valor, 35, 22)
