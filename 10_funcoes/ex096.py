#Faça um programa que tenha uma função chamada área(), que receba as demensões de um terreno reangular (largura e comprimento) e mostre a área do terreno.
def area(largura, comprimento):
    area = largura * comprimento
    print(f'A área de um terreno com {largura}x{comprimento} é de {area}m².')


largura = float(input('Digite a largura do terreno (M): '))
comprimento = float(input('Digite o comprimento do terreno (M): '))

area(largura, comprimento)
