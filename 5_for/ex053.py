#Crie um programa que leia um frase qualquer e diga se essa frase é um palíndromo, desconsiderando os espaços.
frase = str(input('Digite uma frase: ')).strip().split()
frase_sem_esp = ''.join(frase)

print(f'{frase_sem_esp} invertido fica {frase_sem_esp[::-1]}')

if frase_sem_esp == frase_sem_esp[::-1]:
    print('Por isso é um palídromo.')
else:
    print('Por isso não é um palídromo.')
