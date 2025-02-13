#Faça um programa que leia algo pelo teclado e mostre na tela seu tipo primitivo e todas as informações possíveis sobre ela.
x = input('Digite algo: ')

print(f'O tipo primitivo desse valor é {type(x)}')
print(f'Só tem espaços? {x.isspace()}', )
print(f'É um número? {x.isnumeric()}')
print(f'É alfabético? {x.isalpha()}')
print(f'É alfanumérico? {x.isalnum()}')
print(f'Está em maiúscula? {x.isupper()}')
print(f'Está em minúsculas? {x.islower()}')
print(f'Está capitalizada? {x.istitle()}')
