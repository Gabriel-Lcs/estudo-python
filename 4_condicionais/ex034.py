#Escreva um programa que pergunte o salário de um funcionário e calcule seu aumento. Para salários superiores a R$1.250,00, calcule um aumento de 10%. Para os inferiores ou iguais, o aumento é de 15%.
salario = float(input('Digite o seu salário: '))

if salario > 1250:
    novoSal = salario * 1.10
    print(f'O salário de R${salario:.2f} com o aumento de 10% fica R${novoSal:.2f}')
else:
    novoSal = salario * 1.15
    print(f'O salário de R${salario:.2f} com o aumento de 15% fica R${novoSal:.2f}')
