#Faça um programa que tenha uma lista chamada números e duas funções chamadas sorteia() e somaPar(). A primeira função vai sortear 5 números e vai coloca-los dentro da lista e a segunda função vai mostrar a soma entre todos os valores pares sorteados pela função anterior.
from time import sleep
from random import randint
numeros = []

def sorteia(num):
    for i in range(0, 5):
        num.append(randint(1, 10))

    print('Sorteando 5 valores da lista: ', end='')
    
    for i in num:
        print(i, end=' ', flush=True)
        sleep(0.3)

def somaPar(num):
    somaPar = 0
    for i in range(0, len(num)):
        if num[i] % 2 == 0:
            somaPar += num[i]

    print(f'\nA soma dos valores pares de {num} é {somaPar}')


sorteia(numeros)
somaPar(numeros)
