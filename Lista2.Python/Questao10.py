# 10) Escreva um algoritmo que leia um valor inicial A e imprima a seqüência de valores do cálculo de
# A! e o seu resultado. Ex: 5! = 5 X 4 X 3 X 2 X 1 = 120 

a = int(input("Digite o valor que voce deseja saber o Fatorial dele:"))

resultado = 1
sequencia = []

for i in range(a, 0, -1) :
        resultado *= i
        sequencia.append(i)

print(a, "! =", resultado)