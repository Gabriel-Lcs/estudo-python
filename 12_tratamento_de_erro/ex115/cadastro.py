def cadastro():
    print('-' * 40)
    print('CADASTRO'.center(40))
    print('-' * 40)
    
    nome = str(input('Nome: ')).strip().title()
        
    while True:
        idade = str(input('Idade: '))
        if idade.isnumeric():
            int(idade)
            break
        else:
            print('ERRO! Por favor coloque uma idade válida.')

    with open('12_tratamento_de_erro/ex115/dados.txt', 'a', encoding='utf8') as arquivo:
        arquivo.write(f'{nome},')
        arquivo.write(f'{idade}\n')
    
    print(f'Registro de {nome} adicionado.')


def pessoasCadastradas():
    print('-' * 40)
    print('PESSOAS CADASTRADAS'.center(40))
    print('-' * 40)

    try:
        with open('12_tratamento_de_erro/ex115/dados.txt', 'r', encoding='utf8') as arquivo:
            for i in arquivo:
                partes = i.split(',')
                partes[1] = partes[1].replace('\n', '')

                print(f'{partes[0]:<30}{partes[1]} anos')
    except FileNotFoundError:
        print('Nenhum arquivo foi encontrado')
