#Refaça o desafio 009, mostrando a tabuada de um número que o usuário escolher, só que agora utilizando um faço for.
n = int(input('Digite um número: '))

for i in range(1, 11):
    print(f'{n} x {i} = {n * i}')
