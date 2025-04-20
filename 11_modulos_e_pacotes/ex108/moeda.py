#Adapte o código do desafio 107, criando uma função adicional, chamada moeda() que consiga mostrar os valores como um valor monetário formatado
def aumentar(preco = 0, porcentagem = 0):
    resposta = preco * ((100 + porcentagem)/100)
    return resposta


def diminiuir(preco = 0, porcentagem = 0):
    resposta = preco * ((100 - porcentagem)/100)
    return resposta


def dobro(preco):
    resposta = preco * 2
    return resposta


def metade(preco):
    resposta = preco / 2
    return resposta


def cifrao(preco = 0, moeda = 'R$'):
    return f'{moeda}{preco:.2f}'.replace('.', ',')
