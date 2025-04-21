#Crie um pequeno sistema modularizado que permita cadastrar pessoas pelo seu nome e idade em um arquivo de texto simples. O sistema só vai ter 2 opções: cadastrar uma nova pessoa e listar todas as pessoas cadastradas.
from cadastro import cadastro, pessoasCadastradas

while True:
    print('-' * 40)
    print('MENU PRINCIPAL'.center(40))
    print('-' * 40)
    print('1 - Pessoas cadastradas')
    print('2 - Cadastrar pessoa')
    print('3 - Sair')
    print('-' * 40)
    while True:
        esc = input('Escolha sua opção: ')
        if esc.isnumeric():
            esc = int(esc)
            if esc < 1 or esc > 3:
                print('ERRO! Escolha um número válido')
            else:
                break
        else:
            print('ERRO! Escolha um número válido')
          
    if esc == 1:
        pessoasCadastradas()
    elif esc == 2:
        cadastro()
    elif esc == 3:
        print('Programa finalizado')
        break
