#Faça um programa que leia a largura e altura de uma parede em metros, calcule a sua área e a quantidade de tinta necessária para pintá-la, sabendo que a cada litro de inta, pinta uma área de 2m².
altura = float(input('Digite a altura da parede: '))
largura = float(input('Digite a largura da parede: '))

area = altura * largura

print(f'A área da parede é de {area}M² e será necessário {area/2} litros de tinta.')
