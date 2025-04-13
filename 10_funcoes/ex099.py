#Faça um programa que tenha uma função chamada maior(), que receba vários parâmetros com valores inteiros. Seu programa tem que analisar todos os valores e dizer qual deles é o maior.
from time import sleep

def maior(* num):
    print('Analisando os valores passados...')
    
    maior = 0
    
    for i in range(0, len(num)):
        print(num[i], end=' ', flush=True)
        sleep(0.3)

        if i == 0:
            maior = num[i]
        else:
            if num[i] > maior:
                maior = num[i]

    print(f'| Foram informados {len(num)} ao todo.')
    print(f'O maior valor informado foi {maior}')
    print('-=' * 20)


maior(2, 9, 4, 5, 7, 1)
maior(4, 7, 0)
maior(1, 2)
maior(6)
maior()
