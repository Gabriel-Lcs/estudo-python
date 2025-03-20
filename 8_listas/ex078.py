# Faça um programa que leia 5 valores númericos e guarde-os emuma lista. No final, mostre qual foi o maior e o menor valor digitado e as suas respectivas posições na lista.
lista = []

for i in range(1,6):
    lista.append(int(input(f'Digite o {i}° valor: ')))

print(f'A lista digitada foi: {lista}')

print(f'O maior valor foi {max(lista)} nas posições:', end=' ')

for j in range(0,len(lista)):
    if lista[j] == max(lista):
        print(j, end=' ')

print(f'\nO menor valor foi {min(lista)} nas posições:', end=' ')

for k in range(0,len(lista)):
    if lista[k] == min(lista):
        print(k, end= ' ')    
