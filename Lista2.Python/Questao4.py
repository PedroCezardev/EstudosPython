# 4) Escrever um algoritmo que leia uma quantidade desconhecida de números e conte quantos deles
# estão nos seguintes intervalos: [0-25], [26-50], [51-75] e [76-100]. A entrada de dados deve
# terminar quando for lido um número negativo. 

valores = []
intervalo1 = []
intervalo2 = []
intervalo3 = []
intervalo4 = []

while True:
    valor = int(input("Digite um valor (ou um número negativo para sair): "))

    if valor < 0:
        break
    
    valores.append(valor)

    if valor >= 0 and valor <= 25:
        intervalo1.append(valor)
    elif valor >= 26 and valor <= 50:
        intervalo2.append(valor)
    elif valor >= 51 and valor <= 75:
        intervalo3.append(valor)
    elif valor >= 76 and valor <= 100:
        intervalo4.append(valor)
    else:
        print("Digite um valor entre 0 e 100. Tente novamente.")

quantidade_intervalo1 = len(intervalo1)
quantidade_intervalo2 = len(intervalo2)
quantidade_intervalo3 = len(intervalo3)
quantidade_intervalo4 = len(intervalo4)

print("Valores:", valores)
print("Quantidade de Valores [0-25]:", quantidade_intervalo1)
print("Quantidade de Valores [26-50]:", quantidade_intervalo2)
print("Quantidade de Valores [51-75]:", quantidade_intervalo3)
print("Quantidade de Valores [76-100]:", quantidade_intervalo4)
