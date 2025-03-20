# Crie um programa onde o usuário possa digitar vários valores numéricos e cadastre-os em uma lista. Caso o número já exista lá dentro, ele não será adicionado. No final, serão exibidos todos os valores únicos digitados em ordem crescente.
numeros = []

while True:
    valores = int(input('Digite um valor: '))

    if valores not in numeros:
        numeros.append(valores)
    else:
        print('Valor duplicado! Não foi adicionado')

    resp = str(input('Deseja continuar? [S/N] ')).upper()[0]

    if resp == 'N':
        break

print(f'Você digitou os valores: {sorted(numeros)}')
