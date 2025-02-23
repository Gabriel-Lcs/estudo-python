#Faça um programa que leia o sexo de uma pessoa, mas só aceite os valores 'M' ou 'F'. Caso esteja errado, pela a digitação novamente até ter o valor correto.
sexo = str(input('Digite seu sexo [M/F]: ')).upper()

while sexo != 'M' and sexo != 'F':
    print('Opção inválida')
    sexo = str(input('Digite seu sexo novamente [M/F]: ')).upper()

if sexo == 'M':
    print('Sexo masculino.')
else:
    print('Sexo feminino.')
