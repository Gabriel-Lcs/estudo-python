#Adapte o código do desafio 107, criando uma função adicional, chamada moeda() que consiga mostrar os valores como um valor monetário formatado
import moeda

valor = float(input('Digite o preço: R$'))

print(f'A metade de {moeda.cifrao(valor)} é {moeda.cifrao(moeda.metade(valor))}')
print(f'O dobro de {moeda.cifrao(valor)} é {moeda.cifrao(moeda.dobro(valor))}')
print(f'Aumentando 10% de {moeda.cifrao(valor)} é {moeda.cifrao(moeda.aumentar(valor, 10))}')
print(f'Diminuindo 13% de {moeda.cifrao(valor)} é {moeda.cifrao(moeda.diminiuir(valor, 13))}')
