# 8) Escreva um algoritmo que leia três valores inteiros e diferentes e mostre-os em ordem
# decrescente.

valorA = int(input("Digite um valor A: "))
valorB = int(input("Digite um valor B: "))
valorC = int(input("Digite um valor C: "))

# Primeiro, garantir que valorA seja o maior
if valorA < valorB:
    valorA, valorB = valorB, valorA
if valorA < valorC:
    valorA, valorC = valorC, valorA

# Agora, garantir que valorB seja o segundo maior
if valorB < valorC:
    valorB, valorC = valorC, valorB
    
print("Os valores ordenados são: ", valorA, valorB, valorC);

# podemos ordenar também com a propriedade 'sorted', como na forma seguinte:

# if a != b and a != c and b != c:
#     valores = [a, b, c]
#     ordenados = sorted(valores)
#     print(ordenados)
# else :
#     print("Algum ou Alguns valores sao Iguais. Tente Novamente")