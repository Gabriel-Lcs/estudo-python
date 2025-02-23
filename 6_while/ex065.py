#Crie um programa que leia vários números inteiros pelo teclado. No final da execução, mostre a média entre todos os valores e qual foi o maior e o menor valores lidos. O programa deve perguntar ao usuário se ele quer ou não continuar a digitar valores.
n = int(input('Digite um número: '))
opcao = str(input('Deseja continuar a digitar números [S/N] ? ')).upper()
maior = n
menor = n
soma = n
c = 1

while opcao != 'N':
    n = int(input('Digite um número: '))
    opcao = str(input('Deseja continuar a digitar números [S/N] ? ')).upper()

    if n >= maior :
        maior = n
    else:
        menor = n

    c += 1
    soma += n

media = soma / c

print(f'Você digitou {c} números e a média entre os números foi {media}')
print(f'O maior número foi {maior} e o menor foi {menor}')
