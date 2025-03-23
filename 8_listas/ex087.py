#Aprimore o desafio anterior, moestrando no final: A)A soma de todos os valores pares digitados. B)A soma dos valores da terceira coluna. C)O maior valor da segunda linha.
matriz = [[], [], []]
soma_par = 0
soma_coluna = 0

for l1 in range(0, 3):
    matriz[0].append(int(input(f'Digite um valor para [0, {l1}]: ')))

for l2 in range(0, 3):
    matriz[1].append(int(input(f'Digite um valor para [1, {l2}]: ')))

for l3 in range(0, 3):
    matriz[2].append(int(input(f'Digite um valor para [2, {l3}]: ')))

print('-' * 30)
for l in range(0, 3):
    for c in range(0, 3):
        print(f'[{matriz[l][c]:^5}]', end='')

        if matriz[l][c] % 2 == 0:
            soma_par += matriz[l][c]

        if c == 0:
            maior_segunda_linha = matriz[1][c]
        else:
            if matriz[1][c] > maior_segunda_linha:
                maior_segunda_linha = matriz[1][c]
    
    soma_coluna += matriz[l][2]
    print()
print('-' * 30)

print(f'A soma dos valroes pares é {soma_par}.')
print(f'A soma dos valroes da terceira coluna é {soma_coluna}.')
print(f'O maior valor da segunda linha é {maior_segunda_linha}.')
