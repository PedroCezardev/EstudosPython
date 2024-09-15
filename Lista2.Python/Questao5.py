# 5) Faça um algoritmo estruturado que leia uma quantidade não determinada de números positivos.
# Calcule a quantidade de números pares e ímpares, a média de valores pares e a média geral dos
# números lidos. O número que encerrará a leitura será zero. 

valores = []
pares = []
impares = []

while True:
    valor = int(input("Digite um valor (ou um número negativo para sair): "))

    if valor == 0:
        break

if valor % 2 == 0 :
    pares.append(valor)
else :
    impares.append(valor)

#Somas
soma_pares = sum(pares)
soma_valores = sum(valores)

#Quantidades
quantidade_valores = len(valores)
quantidade_pares = len(pares)
quantidade_impares = len(impares)

#Medias
media_pares = soma_pares / quantidade_pares
media_valores = soma_valores / quantidade_valores

print("Valores:", valores)
print("Quantidade de Números Pares:", quantidade_pares)
print("Quantidade de Números Ímpares:", quantidade_impares)
print("Média Geral:", media_valores)
print("Média de Números Pares:", media_pares)