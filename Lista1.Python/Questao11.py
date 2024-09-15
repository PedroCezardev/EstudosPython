# 11) Elabore um algoritmo que calcule o que deve ser pago por um produto, considerando o preço
# normal deetiqueta e a escolha da condição de pagamento. Utilize os códigos da tabela a seguir
# para ler qual acondição de pagamento escolhida e efetuar o cálculo adequado.
# Código Condição de pagamento

# 1 À vista em dinheiro ou cheque, recebe 10% de desconto
# 2 À vista no cartão de crédito, recebe 15% de desconto
# 3 Em duas vezes, preço normal de etiqueta sem juros
# 4 Em duas vezes, preço normal de etiqueta mais juros de 10%

produto = input("Digite o nome do produto:")
preco_etiqueta = float(input(f"Qual o preço do produto {produto}:"))
print("Formas de Pagamento:")
print("Dinheiro/Cheque, Cartao de Credito, Parcelado 2x e Parcelado 3x")
forma_pagamento = input("Qual vai ser a Forma de Pagamento:")

if forma_pagamento == "Dinheiro/Cheque" :
    preco_pago = preco_etiqueta - (preco_etiqueta * 0.10)
    print("Produto: ", produto)
    print("Forma de Pagamento: ", forma_pagamento)
    print(f"Preço a ser Pago: ", preco_pago)
elif forma_pagamento == "Cartao de Credito" :
    preco_pago = preco_etiqueta - (preco_etiqueta * 0.15)
    print("Produto: ", produto)
    print("Forma de Pagamento: ", forma_pagamento)
    print(f"Preço a ser Pago: ", preco_pago)
elif forma_pagamento == "Parcelado 2x" :
    preco_pago = preco_etiqueta
    print("Produto: ", produto)
    print("Forma de Pagamento: ", forma_pagamento)
    print(f"Preço a ser Pago: ", preco_pago) 
else :
    preco_pago = preco_etiqueta + (preco_etiqueta * 0.10)
    print("Produto: ", produto)
    print("Forma de Pagamento: ", forma_pagamento)
    print(f"Preço a ser Pago: ", preco_pago) 
   

