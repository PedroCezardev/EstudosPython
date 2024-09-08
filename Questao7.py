# 7) Faça um algoritmo que leia uma variável e some 5 caso seja par ou some 8 caso seja ímpar,
# imprimir o resultado desta operação.

valorA = int(input("Digite um valor: "));

if (valorA % 2 == 0):
    valorFinal = valorA + 5;
    print("O número é par, entao a soma de ", valorA, "+ 5 é:", valorFinal);
elif (valorA % 2 != 0):
    valorFinal = valorA + 8;
    print("O número é impar, entao a soma de ", valorA, "+ 8 é:", valorFinal);
else:
    print("Número inválido, por favor digite um número inteiro.")