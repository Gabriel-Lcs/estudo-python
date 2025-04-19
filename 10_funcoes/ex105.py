#Faça um programa que tenha uma função chamada notas() que pode receber várias notas de alunos e vai retornar um dicionário com as seguintes informações: - Quantidade de notas. - A maior nota. - A menor nota. - A média da turma. -A situação(opcional). Adicione também as docstrings da função.
def notas(*num, sit=False):
    '''
    -> Função que analisa notas de vários alunos
        :parâmetro num: todos as notas que irão ser analisadas, podem ser várias
        :parâmetro sit: mostra a situação da turma, parâmetro opcional
        :return: o dicionário com as notas
    '''
    nota_aluno = {}
    nota_aluno['Total_notas'] = len(num)

    soma = 0
    for i in range(0, len(num)):
        if i == 0:
            maior = menor = num[0]
        else:
            if num[i] > maior:
                maior = num[i]
            if num[i] < menor:
                menor = num[i]
        
        soma += num[i]

    nota_aluno['Maior'] = maior
    nota_aluno['Menor'] = menor
    nota_aluno['Média'] = soma/len(num)

    if sit == True:
        if nota_aluno['Média'] >= 7:
            nota_aluno['Situação'] = 'Boa'
        elif 4 <= nota_aluno['Média'] < 7:
            nota_aluno['Situação'] = 'Rasoável'
        else:
            nota_aluno['Situação'] = 'Ruim'

    return nota_aluno


resp = notas(5.5, 2.6, 4.4, 10, 8)
print(resp)
#help(notas)
