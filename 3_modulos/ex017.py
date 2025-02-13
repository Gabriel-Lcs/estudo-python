#Faça um programa que leia o comprimento do cateto oposto e do adjacente de um triângulo retângulo, calcute e mostre o comprimento da hipotenusa.
import math
catetoO = float(input("Cateto oposto: "))
catetoA = float(input("Cateto adjacente: "))

print(f'{math.hypot(catetoA, catetoO):.2f}')
