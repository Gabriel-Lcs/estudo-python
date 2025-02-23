#Melhore o desafio 061, perguntando para o usuário se ele quer mostrar mais alguns termos. O programa encerra quando ele disser que quer mostrar 0 termos.
primeiro_termo = int(input('Digite o primeiro termo: '))
razao = int(input('Digite a razão: '))

cont = 1
total = 0
termo = 10

while termo != 0:
    total += termo
    while cont < total:
        primeiro_termo += razao
        print(primeiro_termo)
        cont += 1

    termo = int(input('Digite quantos termos a mais você quer ver: '))
