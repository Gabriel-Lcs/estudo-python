#Refaça o exercício 035 dos triângulos. Acrescentando o recurso de mostrar que tipo de triângulo será formado: - Equilátero: todos os lados iguais. - Isóceles: dois lados iguais. - Escaleno: todos os lados diferentes.
l1 = float(input('Digite o primeiro lado do triângulo: '))
l2 = float(input('Digite o segundo lado do triângulo: '))
l3 = float(input('Digite o terceiro lado do triângulo: '))

if (l1 + l2) > l3 and (l1 + l3) > l2 and (l2 + l3) > l1:
    print('Formam um triângulo.')
    if l1 == l2 == l3:
        print('E formam um triângulo EQUILÁTERO.')
    elif l1 == l2 or l1 == l3 or l2 == l3:
        print('E formam um triângulo ISÓCELES.')
    else:
        print('E formam um triângulo ESCALENO.')
else:
    print('Não formam um triângulo.')
