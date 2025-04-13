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