# Crie um programa que leia nome e duas notas de vários alunos e guarde tudo em uma lista composta. No final, mostre um boletim contendo a média de cada um e permita que o usuário possa mostrar as notas de cada aluno individualmente.
aluno = []
turma = []

while True:
    aluno.append(str(input('Nome do aluno: ')).capitalize())
    aluno.append(float(input('Nota 1: ')))
    aluno.append(float(input('Nota 2: ')))

    turma.append(aluno[:])
    aluno.clear()

    resp = str(input('Deseja continuar? [S/N] ')).upper()[0]
    if resp == 'N':
        break

print('*' * 30)
print(f'{"N°":<4}{"NOME":<10}{"MÉDIA":>8}')
print('-' * 30)

for i in range(0, len(turma)):
    media = (turma[i][1] + turma[i][2]) / 2

    print(f'{i:<4}{turma[i][0]:<10}{media:>8.1f}')

print('-' * 30)

while True:
    consulta = int(input('Mostrar notas de qual aluno? (999 interrompe): '))

    if consulta > len(turma) - 1:
        if consulta == 999:
            print('Programa finalizado!')
            break
            
        print('Aluno inválido.')
    else:
        print(f'As notas de {turma[consulta][0]} são {turma[consulta][1:]}')
