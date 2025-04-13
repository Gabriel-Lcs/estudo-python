#Faça um programa que tenhauma função chamada contador() que rebeca três parâmetros: início, fim e passo e realize a contagem. Seu programa tem que realizar três contagens através da função criada: A) De 1 até 10, de 1 em 1. B) De 10 até 0, de 2 em 2. C)Uma contagem personalizada.
from time import sleep

def contador(inicio, fim, passo):
    if passo == 0:
        passo = 1
    elif passo < 0:
        passo *= -1

    print(f'Contagem de {inicio} até {fim} de {passo} em {passo}')
    if inicio <= fim:
        while inicio <= fim:
            print(inicio, end=' ', flush=True)
            sleep(0.5)
            
            inicio += passo  
    else:
        while fim <= inicio:
            print(inicio, end=' ', flush=True)
            sleep(0.5)
            
            inicio -= passo 

    print()
    print(f'-' * 35)
            

contador(1, 10, 1)
contador(10, 0, 2)

print('Agora é sua vez de personalizar a contagem!')
inicio = int(input('Inicio: '))
fim = int(input('Fim: '))
passo = int(input('Passo: '))

contador(inicio, fim, passo)
