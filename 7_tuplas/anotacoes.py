# ANOTAÇÕES SOBRE TUPLAS
tupla = ("Hambúrguer", "Suco", "Pizza", "Pudim")

# Mostrar todos os índices
for i in tupla:
    print(i)

print(20 * '-')

for pos, i in enumerate(tupla):
    print(f'{i} na posição {pos}')

print(20 * '-')

for i in range(0, len(tupla)):
    print(f'{tupla[i]} na posição {i}')

print(20 * '-')

# Formatação sem os parênteses e aspas com JOIN:
x = " ".join(tupla)
print(x)

# Mostrando com ídices:
print(tupla[2]) # Irá printar "Pizza"

print(tupla[-3]) # Irá printar "Suco"

print(tupla[1:3]) # Irá printar "Suco" "Pizza"

print(tupla[:2]) # Irá printar do início ao índice 2 -> "Hambúrguer" "Suco"

# Ordenar a tupla
print(sorted(tupla))

#Procurar elemento
print(tupla.index('Pizza'))
