#Crie um programa que vai ler vários números e colocar em uma lista. Depois disso, crie duas listas extras que vão conter apenas os valores pares e os alores ímpares digitados, respectivamente. Ao final mostre o conteúdo das três listas geradas. 
numeros = []
par = []
impar = []

while True:
    numeros.append(int(input('Digite um valor: ')))

    resp = str(input('Deseja continuar? [S/N] ')).upper()[0]
    if resp == 'N':
        break

for i in range(0, len(numeros)):
    if numeros[i] % 2 == 0:
        par.append(numeros[i])
    else:
        impar.append(numeros[i])

print(f'A lista compelta é: {numeros}')
print(f'A lista dos número pares é: {par}')
print(f'A lista dos número ímpares é: {impar}')
