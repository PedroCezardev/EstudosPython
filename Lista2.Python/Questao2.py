# Desenvolver um algoritmo que leia a altura de 15 pessoas. Este programa deverá calcular e
# mostrar :
# a. A menor altura do grupo;
# b. A maior altura do grupo; 

alturas = []

for i in range(1, 16):
    altura = float(input(f"Digite a altura {i} em metros: "))
    if altura > 2.72 or altura <= 0.5:
        print("Altura Inválida")
    else:
        alturas.append(altura)


if alturas: #Se alturas for true (tiver valores...)
    maior_altura = max(alturas)
    menor_altura = min(alturas)
    print("A maior altura é:", maior_altura)
    print("A menor altura é:", menor_altura)
else:
    print("Nenhuma altura válida foi inserida.")
