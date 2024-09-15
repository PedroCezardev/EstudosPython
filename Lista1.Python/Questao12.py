# 12) Escreva um algoritmo que leia o número de identificação, as 3 notas obtidas por um aluno nas
# 3 verificações e a média dos exercícios que fazem parte da avaliação, e calcule a média de
# aproveitamento, usando a fórmula:

# MA := (nota1 + nota 2 * 2 + nota 3 * 3 + ME)/7
# A atribuição dos conceitos obedece a tabela abaixo. O algoritmo deve escrever o número do aluno,
# suas notas, a média dos exercícios, a média de aproveitamento, o conceito correspondente e a
# mensagem 'Aprovado' se o conceito for A, B ou C, e 'Reprovado' se o conceito for D ou E.

# Média de aproveitamento Conceito
# >= 90 A
# >= 75 e < 90 B
# >= 60 e < 75 C
# >= 40 e < 60 D
# < 40 E 

id_aluno = int(input("Qual o Número de Identificação do aluno: "))

nota1 = float(input("Digite a primeira nota: "))
nota2 = float(input("Digite a segunda nota: "))
nota3 = float(input("Digite a terceira nota: "))

# Verifica se alguma nota é menor que zero
if nota1 < 0 or nota2 < 0 or nota3 < 0:
    print("Nota menor que zero. Tente novamente.")
else:
    # Calcula a média e a média de aproveitamento
    media = (nota1 + nota2 + nota3) / 3
    media_aproveitamento = (nota1 + nota2 * 2 + nota3 * 3 + media) / 7

    # Definindo o conceito com base na média de aproveitamento
    if media_aproveitamento >= 90:
        conceito = "A"
    elif media_aproveitamento >= 75:
        conceito = "B"
    elif media_aproveitamento >= 60:
        conceito = "C"
    elif media_aproveitamento >= 40:
        conceito = "D"
    else:
        conceito = "E"

    # Definindo a situação acadêmica com base no conceito
    if conceito == "A" or conceito == "B" or conceito == "C":
        situacao = "Aprovado!"
    else:
        situacao = "Reprovado!"

    # Imprimindo os resultados
    print("Número de Identificação: ", id_aluno)
    print("Nota 1: ", nota1)
    print("Nota 2: ", nota2)
    print("Nota 3: ", nota3)
    print("Média: ", media)
    print("Média de Aproveitamento: ", media_aproveitamento)
    print("Conceito: ", conceito)
    print("Situação Acadêmica: ", situacao)
