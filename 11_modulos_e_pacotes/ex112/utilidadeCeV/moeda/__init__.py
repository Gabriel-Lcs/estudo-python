def aumentar(preco = 0, porcentagem = 0, formatar = False):
    resposta = preco * ((100 + porcentagem)/100)
    if formatar == True:
        resposta = cifrao(resposta)

    return resposta


def diminiuir(preco = 0, porcentagem = 0, formatar = False):
    resposta = preco * ((100 - porcentagem)/100)
    if formatar == True:
        resposta = cifrao(resposta)

    return resposta


def dobro(preco, formatar = False):
    resposta = preco * 2
    if formatar == True:
        resposta = cifrao(resposta)

    return resposta


def metade(preco, formatar = False):
    resposta = preco / 2
    if formatar == True:
        resposta = cifrao(resposta)

    return resposta


def cifrao(preco = 0, moeda = 'R$'):
    return f'{moeda}{preco:.2f}'.replace('.', ',')


def resumo(preco = 0, aumento = 0, reducao = 0):
    print('-' * 35)
    print('RESUMO DOS VALORES'.center(35))
    print('-' * 35)
    print(f'Preço analisado: \t{cifrao(preco)}')
    print(f'Dobro do preço: \t{dobro(preco, True)}')
    print(f'Metade do preço: \t{metade(preco, True)}')
    print(f'{aumento}% de aumento: \t{aumentar(preco, aumento, True)}')
    print(f'{reducao}% de redução: \t{diminiuir(preco, reducao, True)}')
    print('-' * 35)
