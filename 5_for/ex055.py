#Faça um programa que leia o peso de cinco pessoas. No final, mostre qual foi o maior e o menor peso lidos.
peso = float(input('Digite seu peso: KG '))

maior_peso = 0
menor_peso = peso

for i in range(0,4):
    peso = float(input('Digite seu peso: KG '))

    if peso > maior_peso:
        maior_peso = peso
    elif peso < menor_peso:
        menor_peso = peso

print(f'O maior peso é {maior_peso:.2f} Kg.\nO menor peso é {menor_peso:.2f} Kg.')
