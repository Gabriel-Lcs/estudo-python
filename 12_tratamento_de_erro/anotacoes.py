# - TRY EXECPT -
try:                            #Serve para tentar
    a = int(input('Digite o numerador: '))
    b = int(input('Digite o denominador: '))
    r = a/b
except ValueError:              #Serve para SE der problema
    print('Erro pois não foi digitado um número')
except ZeroDivisionError:
    print('Erro não é possível dividir por zero.')
except KeyboardInterrupt:
    print('\nO usuário decidiu encerrar o programa')
else:                           #Serve para caso não dê problema
    print(f'O resultado é {r:.1f}')
finally:                        #Vai acontecer se deu certo ou se deu erro (VAI ACOTNECER SEMPRE)
    print('Volte sempre.')



# except Exception as erro:       #Serve para SE der problema
#     print('Infelizmente tivemos um problema')
#     print(f'Tivemos o problema de {erro.__class__}')