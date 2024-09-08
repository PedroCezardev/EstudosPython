# Escreva um algoritmo que leia o número de litros vendidos e o tipo de combustível (codificado da seguinte forma: 
# E-etanos G-gasolina), calcule e imprima o valor a ser pago pelo cliente sabendo-se que o preço do litro da gasolina 
# é R$ 5,80 e o preço do litro do etanol é R$ 4,90.

litros = float(input("Quantos litros você encheu? "))
tipo = input("Digite o tipo de combustivel: ")

if tipo == "G" or "g": # se o valor do tipo for igual a G ou g ele vai executar o codigo a baixo
    valor = litros * 5.80 # declarando uma variavel 'valor' para receber o calculo de litros * o valor da gasolina
    print(f"Voce precisa pagar:  {valor} ") # passando pra o usuario o valor que ele precisa pagar, com a variavel 'valor'
    
elif tipo == "E" or "e": # se o valor do tipo for igual a E ou e ele vai executar o codigo a baixo
    valor = litros * 4.90
    print(f"Voce precisa pagar: {valor} ")
    
else: # se o valor do tipo não for igual a nenhum valor acima, ele exibe uma mensagem de erro.
    print("Por favor, digite uma opção válida (G ou E).")
    
# Fazer mais 'elif' para colocar outros tipos de combustíveis, como Alcool 'A', diesel 'D' e Bateria 'B'.
    
# Diferença entre 'AND' E 'OR':
    
if tipo == "G" and "g": # se o valor do tipo for igual a 'G' e 'g' ao mesmo tempo, ele vai executar o codigo a baixo
    valor = litros * 5.80 
    print(f"Voce precisa pagar:  {valor} ")
    
elif tipo == "E" or "e": # se o valor do tipo for igual a 'E' ou 'e' (um de cada vez), ele vai executar o codigo a baixo
    valor = litros * 4.90
    print(f"Voce precisa pagar: {valor} ")
    
# A diferença entre And e Or é que 'and' verifica se é G (maiusculo) e g (menusculo) ao mesmo tempo
# Enquanto, 'Or' verifica se é G (maiusculo) ou g (menusculo), um de cada vez.