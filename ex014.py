#Escreva um programa que conversa uma temperatura digitada em °C e converta para °F.
c = float(input('Digite a temperatura em °C: '))

temp = c * 1.8 + 32

print(f'{c:.1f}°C em Fahrenheit é {temp:.1f}°F.')
