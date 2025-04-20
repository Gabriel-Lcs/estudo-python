def leiaDinheiro(text):
    preco = str(input(text)).replace(',','.').strip()

    while preco.isalpha() == True or preco == '':
        print(f'Erro! "{preco}" não é um valor válido')
        preco = str(input(text)).replace(',','.')

    if preco.isalpha() != True:
        preco = float(preco)
        return preco
