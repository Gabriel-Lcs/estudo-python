#Reescreva a função leiaInt() que fizemos no desafio 104, incluindo agora a possibilidade da digitação de um número de tipo inválido. Aproviete e crie também uma função leiaFloat() com a mesma funcionalidade.
def leiaInt(num):
    while True:
        try:
            inteiro = int(input(num))
        except ValueError:
            print('Erro! Digite um número válido.')
        except KeyboardInterrupt:
            print('\nO usuário preferiu não digitar esse número')
            return 0
        else:
            return inteiro


def leiaFloat(num):
    while True:
        try:
            real = float(input(num))
        except ValueError:
            print('Erro! Digite um número válido.')
        except KeyboardInterrupt:
            print('\nO usuário preferiu não digitar esse número')
            return 0
        else:
            return real


inteiro = leiaInt('Digite um número Inteiro: ')
real = leiaFloat('Digite um número Real: ')
print(f'O valor inteiro digitado foi {inteiro} e o real foi {real}')
