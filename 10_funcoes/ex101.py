#Crie um programa que tenha uma função chamada voto() que vai receber como parâmetro o ano de nascimento de uma pessoa, retornando um valor literal indicando se uma pessoa tem o voto negado, opcional ou obrigatório nas eleições.
def voto(nascimento):
    from datetime import datetime

    idade = datetime.today().year - nascimento
    if idade < 16:
        return f'Com {idade} anos: VOTO NEGADO'
    elif 16 <= idade < 18 or idade > 65:
        return f'Com {idade} anos: VOTO OPCIONAL'
    else:
        return f'Com {idade} anos: VOTO OBRIGATÓRIO'
    
nascimento = int(input('Em que ano você nasceu? '))
print(voto(nascimento))
