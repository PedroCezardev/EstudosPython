# 8) Escreva um algoritmo que leia um valor inicial A e uma razão R e imprima uma seqüência em
# P.A. contendo 10 valores. 

a1 = int(input("Digite o valor Inicial (A1):"))

r = int(input("DIgite o valor da Razão R:"))

print("Sequência em P.A. com 10 valores:")
for n in range(10) :
    an = (a1 + n) * r
    print(an)
