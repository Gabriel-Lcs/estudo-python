#Crie um programa onde o usuário possa digitar 5 valores numéricos e cadastre-os em uma lista, já na posição correta de inserção (sem usar o sort()). No final, mostre a lista ordenada na tela.
numeros = []

for i in range(0, 5):
    n = int(input('Digite um número: '))

    if i == 0:
        numeros.append(n)
    elif n > numeros[-1]:
        numeros.append(n)
    else:
        pos = 0
        while pos < len(numeros):
            if n <= numeros[pos]:
                numeros.insert(pos, n)
                break

            pos += 1

print(f'A ordem dos números é {numeros}')
