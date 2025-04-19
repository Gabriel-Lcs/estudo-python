#Faça um mini sistema que utilize o Interactive Help do python. O usuário vai sigitar o comando e o manual vai aparecer. Quando o usuário digitar a palavra 'FIM', o programa se encerrará.
while True:
    print('-' * 40)
    print('Sistema de ajuda')
    print('-' * 40)

    biblioteca = str(input('Função ou Biblioteca > ')).lower()
    if biblioteca == 'fim':
        print('Pograma finalizado!')
        break
        
    print('-' * 40)
    print(f'Mostrando a biblioteca do {biblioteca}')
    print('-' * 40)
    help(biblioteca)
