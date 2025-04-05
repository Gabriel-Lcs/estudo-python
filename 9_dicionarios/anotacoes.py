#Anotações sobre DICIONÁRIOS:
dados = {
    'nome': 'Pedro',
    'idade': 25
}

print(dados['idade']) #print: 25

#Adicionar um dado novo
dados['sexo'] = 'M'
print(dados)

#Remover um dado
del dados['idade']
print(dados)

print('------------------------------------' * 2)

filme = {
    'titulo': 'Star Wars',
    'ano': 1977,
    'diretor': 'George Lucas'
}

#mostrar os valores -> values
print(filme.values())

#mostrar as chaves -> key
print(filme.keys())

#mostrar os itens -> items
print(filme.items())

for k, v in filme.items():
    print(f'o {k} é {v}')

for i in filme.items():
    print(i)

print('------------------------------------' * 2)
brasil = []
estado1 = {
    'uf': 'Rio de Janeiro',
    'sigla': 'RJ'
}
estado2 = {
    'uf': 'São Paulo',
    'sigla': 'SP'
}

brasil.append(estado1)
brasil.append(estado2)

print(brasil)
print(brasil[0])
print(brasil[0]['uf'])
print(brasil[1]['sigla'])

#Adicionar 3 estados na lista
estado = {}
brasil1 = []
for i in range(0, 3):
    estado['uf'] = str(input('Unidade Federativa: '))
    estado['sigla'] = str(input('Sigla do Estado: '))
    brasil1.append(estado.copy())

for j in brasil1:        #Laço que passa pela lista e acessa cada um dos dicionários
    for k in j.items():  #Laço que passa por cada dos dicionários ("J" se torna o dicionário)
        print(k)
