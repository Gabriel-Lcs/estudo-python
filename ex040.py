#Crie um programa que leia duas notas de um aluno e calcule sua média, mostrando uma mensagem no final, de acordo com a média atingida: - Média abaixo de 5.00: REPROVADO. - Média aentre 5.0 e 6.9: RECUPERAÇÃO. - Média 7.0 ou superior: APROVADO.
n1 = float(input('Digite sua primeira nota: '))
n2 = float(input('Digite sua segunda nota: '))

media = (n1 + n2) / 2

if media < 5.0:
    print(f'Sua média foi {media:.1f} então você está REPROVADO!')
elif media >= 5.0 and media <= 6.9:
    print(f'Sua média foi {media:.1f} então você está de RECUPERAÇÃO!')
else:
    print(f'Parabéns sua média foi {media:.1f}, você está APROVADO')
