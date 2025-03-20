#Crie um programa que vai ler vários números e colocar em uma lista. Depois disso, mostre: A) Quantos números foram digitados. B) A lista de valores, ordenada de forma decrescente. C) Se o valor 5 foi digitador e está ou não na lista.
valores = []

while True:
    valores.append(int(input(f'Digite o {len(valores) + 1}° valor: ')))

    resp = str(input('Deseja adicionar outro número? [S/N]')).upper()[0]
    if resp == 'N':
        break

print(f'Na lista foram adicionados {len(valores)} números')

valores.sort(reverse=True)
print(f'A lista de forma decrescente fica: {valores}')

if 5 in valores:
    print('O número 5 está na lista! Nas posições: ', end='')
    for i in range(0, len(valores)):
        if valores[i] == 5:
            print(i, end='...')
else:
    print('O 5 não faz parte da lista.')
