# 9) Tendo como dados de entrada a altura e o sexo de uma pessoa, construa um algoritmo que
# calcule seu peso ideal, utilizando as seguintes fórmulas:
# ● para homens: (72.7 * h) – 58;
# ● para mulheres: (62.1 * h) – 44.7. 

altura = float(input("Qual sua Altura:"))
sexo = input("Qual seu sexo (M ou F):")

if sexo == "M" :
    peso_ideal = (72.7 * altura) - 58
    print(peso_ideal)
else :
    peso_ideal = (62.1 * altura) - 44.7
    print(peso_ideal)