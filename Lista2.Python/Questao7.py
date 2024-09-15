# 7) Escrever um algoritmo que leia um valor para uma variável N de 1 a 10 e calcule a tabuada de
# N. Mostre a tabuada na forma: 0 x N = 0, 1 x N = 1N, 2 x N = 2N, ..., 10 x N = 10N. 

n = int(input("Digite um valor:"))

if n < 1 :
    print("Número menor que 1 ou maior que 10. Tente Novamente")
else:
    for i in range(1, 11):
        tabuada = n * i
        print(i, " X ", n, " = ", tabuada)
