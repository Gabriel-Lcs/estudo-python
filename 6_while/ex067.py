#Faça um programa que moste a tabuada de vários números, um de cada vez, para cada valor digitado pelo usuário. O programa será interrompido quando o número solicitado for negativo.
while True:
    n = int(input('Deseja ver a tabuada de qual valor? '))
    print("-" * 40)

    if n < 0:
        break

    for i in range(1, 11):
        print(f'{n} x {i:2} = {n * i}')
        
    print("-" * 40)
