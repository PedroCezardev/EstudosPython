# Encontrar o dobro de um número caso ele seja positivo e o seu triplo caso seja negativo,
# imprimindo o resultado. 

input = int(input("Digite um número inteiro: "))

if input > 0:
    resultado = input * 2
    print("O número é positivo, então o Dobro dele é: ", resultado)
else:
    resultado= input * 3 
    print("O número é negativo, então o Triplo dele é: ", resultado)