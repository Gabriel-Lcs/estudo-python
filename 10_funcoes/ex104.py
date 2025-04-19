#Crie uma programa que tenha uma função leiaInt(), que vai funcionar de forma semelhante à função input() do pyhton, só que fazendo a validação para aceitar apenas um valor numérico.
def leiaInt(num):
    n = input(num)

    while n.isnumeric() != True:
        print('Erro! Digite um número válido.')
        n = input(num)

    if n.isnumeric() == True:
        return int(n)


n = leiaInt('Digite um número: ')
print(f'Voce digitou o número {n}')
