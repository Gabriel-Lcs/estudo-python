# Crie um programa que tenha uma tupla com várias palavras (não usar acentos). Depois disso, você deve mostrar, para cada plavra, quais são as suas vogais.
palavras = ('aprender', 'programar', 'casa', 'curso', 'python')

for i in range(0, len(palavras)):
    print(f'\nNa palavra {palavras[i].upper()} temos', end=' ')
    for p in range(0, len(palavras[i])):
        if palavras[i][p] in 'aeiou':
            print(palavras[i][p], end=' ')
