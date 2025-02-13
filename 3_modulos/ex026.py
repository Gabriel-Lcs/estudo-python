#Faça um programa que leia uma frase pelo teclado e mostre: -Quantas vezes aparece a letra "A"; -Em que posição ela aparece a primeira vez; -Em que posição ela a aparece a ultima vez.
n = str(input('Digite o seu nome: ')).upper()

print(f'Qauntidade de "A": {n.count("A")}')
print(f'A letra "A" aparece pela primeira vez na posição: {n.find("A") + 1}')
print(f'A letra "A" aparece pela última vez na posição: {n.rfind("A") + 1}')
