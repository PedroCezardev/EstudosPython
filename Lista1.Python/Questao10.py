# 10) O IMC – Indice de Massa Corporal é um critério da Organização Mundial de Saúde para dar
# umaindicação sobre a condição de peso de uma pessoa adulta. A fórmula é IMC = peso / ( altura )2

# Elabore um algoritmo que leia o peso e a altura de um adulto e mostre sua condição de acordo
# com a tabela abaixo.
# IMC em adultos Condição
# Abaixo de 18,5 Abaixo do peso
# Entre 18,5 e 25 Peso normal
# Entre 25 e 30 Acima do peso
# Acima de 30 obeso

peso = float(input("Qual seu Peso:"))
altura = float(input("Qual sua altura:"))

imc = peso / (altura * altura)

if imc < 18.5 :
    print("Você está ABAIXO DO PESO")
elif imc >= 18.5 and imc < 25 :
    print("Você esá PESO NORMAL")
elif imc >= 25 and imc < 30 :
    print("Você está ACIMA DO PESO")
else:
    print("Você está OBESO")