# 8) Escreva um algoritmo que leia três valores inteiros e diferentes e mostre-os em ordem
# decrescente.

valorA = int(input("Digite um valor A: "))
valorB = int(input("Digite um valor B: "))
valorC = int(input("Digite um valor C: "))

if (valorA > valorB):
    valorA, valorB = valorB, valorA;
    
elif (valorA > valorC):
    valorA, valorC = valorC, valorA;
    
elif (valorB > valorC):
    valorB, valorC = valorC, valorB;
    
print("Os valores ordenados são: ", valorA, valorB, valorC);