#Crie um programa onde o usuário digite uma expressão que use parênteses. Seu aplicativo deverá analisar se a expressão passada está com os parênteses abertos e fechados na ordem correta.
expressao = []
expressao.append(str(input('Digite a expressão matemática: ')))

parentese1 = 0
parentese2 = 0

for i in range(0, len(expressao[0])):
    if expressao[0][i] == '(':
        parentese1 += 1

    if expressao[0][i] == ')':
        parentese2 += 1

if parentese1 == parentese2:
    print('A expressão é válida')
else:
    print('A expressão está inválida')
