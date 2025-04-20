#Modifique as funções que foram criadas no desafio 107 para que elas acitem um parâmetro a mais, iformar se o valor retornado por elas vai ser ou não pela função moeda desenvolvida no desafio 108.
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
