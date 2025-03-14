#O mesmo professor do desafio anterior quer sortear a ordem de apresentação do trabalho dos alunos, faça um programa que leia o nome dos quatro alunos e mostre a ordem sorteada.
from random import shuffle

aluno1 = str(input('Digite o nome do primeiro aluno: '))
aluno2 = str(input('Digite o nome do segundo aluno: '))
aluno3 = str(input('Digite o nome do terceiro aluno: '))
aluno4 = str(input('Digite o nome do quanto aluno: '))

lista = [aluno1, aluno2, aluno3, aluno4]
shuffle(lista)

lista_formatada = ' '.join(lista) 

print(f"A ordem do sorteio foi {lista_formatada}")
