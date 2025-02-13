#Desenvolva um programa que leia o primeiro termo e a razão se uma PA. No final, mostre os 10 primeiros termos dessa progressão.
primeiro_termo = int(input('Digite o primeiro termo: '))
razao = int(input('Digite a razão: '))

utlimo_termo = primeiro_termo + (10 - 1) * razao

for i in range(primeiro_termo, utlimo_termo + 1, razao):
    print(i)
