# 6) Escreva um algoritmo que lê dois valores booleanos (lógicos) e então determina se ambos são
# VERDADEIROS ou FALSOS.

A = (input("Digite se o valor de A é Verdadeiro (true) ou falso (false): ")).strip().lower()

B = (input("Digite se o valor de A é Verdadeiro (true) ou falso (false): "))

if (A == 'true' and B == 'true'):
    valor_booleano = True;
    print("O valor A é", valor_booleano);
    print("O valor B é", valor_booleano);
    
elif (A == 'false' and B == 'false'):
    valor_booleano = False;
    print("O valor A é:", valor_booleano);
    print("O valor B é:", valor_booleano);
    
elif (A == 'true' and B == 'false'):
    valor_true= True;
    valor_false = False;
    print("O valor A é:", valor_true);
    print("O valor B é:", valor_false);
    
elif (A == 'false' and B == 'true'):
    valor_false = False;
    valor_true= True;
    print("O valor A é:", valor_false);
    print("O valor B é:", valor_true);

else:
    print("Opção inválida, por favor digite 'true' ou 'false");