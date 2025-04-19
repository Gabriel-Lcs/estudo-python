#Anotações sobre FUNÇÕES
def mensagem(msg):
    print('-' * 15)
    print(msg)
    print('-' * 15)

def soma(a, b):
    s = a + b
    print(s)

def contador(* num):
    print(num)

def dobra(lista):
    pos = 0
    while pos < len(lista):
        lista[pos] *= 2
        pos += 1

def soma1(* valores):
    s = 0
    for num in valores:
        s += num

    print(valores, s)



mensagem('Olá mundo')

soma(4, 5)

contador(2, 1, 7)
contador(4, 2)
contador(6, 5, 1, 8, 9)

valores = [7, 8, 1, 2, 4]
dobra(valores)
print(valores)

soma1(2, 5)
soma1(2, 4, 6)

#Parte 2
#interactive help
    #help() Mostra tudo sobre a função definida no terminal

def cont(i, f, p):
    """
    -> Faz uma contagem de números:
        :parametro i: Inicio da contagem
        :parametro f: Fim da contagem 
        :parametro p: Passo da contagem 
        :return: sem retorno
    """
    while i <= f:
        print(i, end=' ', flush=True)
            
        i += p 


cont(0, 10, 2)
help(cont)

#Parâmetro opcional:
def somar(a = 0, b = 0, c = 0):
    """
    -> Função para somar elementos
        :parametro a: o primeiro valor
        :parametro b: o segundo valor
        :parametro c: o terceiro valor
        :parametro s: soma todos os elementos
    """
    s = a + b + c
    print(s)

    #com o Parâmetro opcional eu consigo não preencher todos os valores na função, permitidno chamar a função dessas 4 formas, até mesmo vazio
somar(4, 3, 9)                  
somar(4, 3)
somar(4)
somar()

#Escopo de variáveis:
def teste(b):
    global a           #transforma o A de fora de 5 para 8, caso não tivesse o "global" mesmo colocando 8 localmente, fora continuaria com 5.
    a = 8                       
    b += 4
    c = 2


a = 5
teste(a)