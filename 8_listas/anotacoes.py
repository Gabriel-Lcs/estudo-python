# Anotações de sobre LISTAS:

lanche = ['hambúrguer', 'suco', 'pudim', 'pizza']
print(lanche)

# Adicionar um elemento no final
lanche.append('picole')
print(lanche)

# Inserir um elemento em uma posição específica da lista
lanche.insert(0, 'refrigerante')
print(lanche)

# Remover um elemento pelo indice
# del lanche[3] #Tambpem remove, igual ao pop
lanche.pop(3) #lanche.pop() -> Remove o ultimo elemento
print(lanche)

# Remover um elemento pelo nome
lanche.remove('pizza')
print(lanche)

# Criar uma lista
valores = list(range(4,11))
print(valores) #Printa os valores [4, 5, 6, 7, 8, 9, 10], mas os índices são 0, 1, 2, 3, 4, 5, 6

# Ordenação de lista
valores = [2, 8, 5, 4, 9, 3, 0]
print(valores)
valores.sort()
print(valores)

# Ordenar ao contrário
valores.sort(reverse=True)
print(valores)

# Cópia de listas
a = [2, 4, 5, 7]
b = a # Se eu mudar um elemento ele vai mudar nas duas listas
b[1] = 9

print(f'A lista A: {a}')
print(f'A lista B: {b}')

x = [5, 8, 0, 1]
y = x[:] # Y está recebendo todos os valores de X, assim posso alterar algum valor
y[3] = 9

print(f'A lista X: {x}')
print(f'A lista Y: {y}')
