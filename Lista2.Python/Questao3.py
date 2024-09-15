# 3) Desenvolver um algoritmo que leia um número não determinado de valores e calcule e escreva a
# média aritmética dos valores lidos, a quantidade de valores positivos, a quantidade de valores
# negativos e o percentual de valores negativos e positivos. 

valores = []
positivos = []
negativos = []

while True:
    valor = int(input("Digite um valor: "))
    
    valores.append(valor)

    termina = input("Deseja Continuar? Sim ou Nao: ")
    if termina.lower() != "sim":
        break

soma = sum(valores)
quantidade = len(valores)

for valor in valores:
    if valor > 0:
        positivos.append(valor)
    elif valor < 0:
        negativos.append(valor)


quantidade_positivos = len(positivos)
quantidade_negativos = len(negativos)

media = soma / quantidade if quantidade > 0 else 0

percentual_positivos = (quantidade_positivos / quantidade) * 100 if quantidade > 0 else 0
percentual_negativos = (quantidade_negativos / quantidade) * 100 if quantidade > 0 else 0

print("Valores:", valores)
print("Média:", media)
print("Quantidade de Valores Positivos:", quantidade_positivos)
print("Quantidade de Valores Negativos:", quantidade_negativos)
print("Percentual de Valores Positivos:", percentual_positivos)
print("Percentual de Valores Negativos:", percentual_negativos)
