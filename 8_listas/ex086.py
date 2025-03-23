#Crie um programa que crie uma matriz de dimensão 3x3 e preencha com valores lidos pelo teclado. No final moestre a matriz na tela, com a formatação correta.
matriz = [[], [], []]

for i in range(0, 3):
    matriz[0].append(int(input(f'Digite um vlaor para [0, {i}]: ')))

for j in range(0, 3):
    matriz[1].append(int(input(f'Digite um vlaor para [1, {j}]: ')))

for k in range(0, 3):
    matriz[2].append(int(input(f'Digite um vlaor para [2, {k}]: ')))

print('-' * 30)

for l in range(0, 3):
    for c in range(0, 3):
        print(f'[{matriz[l][c]:^5}]', end='')

    print()
