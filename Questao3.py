# 3) Faça um algoritmo para receber um número qualquer e informar na tela se é par ou ímpar. 

input = int(input("Digite um Número Inteiro: "))

if input % 2 == 0:
    print("O número ", input, " é par")
else:
    print("O número ", input, " é impar")