#Crie um programa que leia o nome de uma cidade e diga se ela começa ou não com o nome "Santo".
n = str(input('Digite o nome da cidade: ')).strip().upper().split()

print('SANTO' in n[0])
