#Escreva um programa que leia um número n inteiro qualquer e mostre na tela os n primeiros elementos de uma Sequência de Fibonacci.
n = int(input('Digite um número: '))

t1 = 0
t2 = 1
print(t1, t2, end=' ')

cont = 3
while cont <= n:
    t3 = t1 + t2

    print(t3, end=' ')

    t1 = t2
    t2 = t3
    cont += 1
