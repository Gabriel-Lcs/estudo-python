# Desenvolva um programa que leia quatro valores pelo teclado e guarde-os em uma tupla, no final mostre: A)Quantas vezes apareceu o valor 9. B)Em que posição foi digitado o primeiro valor 3. C)Quais foram os números pares.
n1 = int(input('Digite o primeiro número: '))
n2 = int(input('Digite o segundo número: '))
n3 = int(input('Digite o terceiro número: '))
n4 = int(input('Digite o quarto número: '))

numeros = (n1, n2, n3, n4)

print(f'O número 9 aparece {numeros.count(9)} vezes')
if 3 in numeros:
    print(f'O número 3 aparece na {numeros.index(3) + 1}° posição')
else:
    print(f'O número 3 não foi digitado em nenhuma posição')

print('Os números pares digitados foram:', end=' ')
par = 0
for i in range(0, len(numeros)):
    if numeros[i] % 2 == 0:
        par += 1
        print(numeros[i], end=' ')

if par == 0:
    print('nenhum')
