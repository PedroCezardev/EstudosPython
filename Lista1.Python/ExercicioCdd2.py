# dados os valores de horários abaixo, decifre a lógica e faça um código para executar
# entrada01: 3:45
# entrada02: 14:20
# saída: 6:05

hora1 = int(input("Digite a hora da primeira entrada: "))
minuto1 = int(input("Digite os minutos: "))

hora2 = int(input("Digite a hora da segunda entrada: "))
minuto2 = int(input("Digite os minutos: "))

horaEntrada = hora1 + hora2;
minutosEntrada = minuto1 + minuto2;

print(hora2, minuto2);

print(horaEntrada, minutosEntrada);

ultimaEntradaTempoSaidaHora = horaEntrada + hora2;
ultimaEntradaTempoSaidaMinuto = minutosEntrada + minuto2;

print(ultimaEntradaTempoSaidaHora, ultimaEntradaTempoSaidaMinuto);

# Ajuste de minutos
if ultimaEntradaTempoSaidaMinuto >= 60:
    ultimaEntradaTempoSaidaHora += ultimaEntradaTempoSaidaMinuto // 60
    ultimaEntradaTempoSaidaMinuto = ultimaEntradaTempoSaidaMinuto % 60

# Ajuste de horas
if ultimaEntradaTempoSaidaHora >= 24:
    ultimaEntradaTempoSaidaHora = ultimaEntradaTempoSaidaHora % 24

if (ultimaEntradaTempoSaidaHora > 23 or ultimaEntradaTempoSaidaMinuto > 59):
    ultimaEntradaTempoSaidaHora - 23;
    ultimaEntradaTempoSaidaMinuto - 60;
    print(ultimaEntradaTempoSaidaHora, ultimaEntradaTempoSaidaMinuto);


#horaTotal = horaEntrada + minutosEntrada;

#print(horaTotal)

#horaFinal = horaMinuto2 + horaTotal;

#print(horaFinal);

# o resultado dará 17:65, porém nao existe essa hora
# entao trataremos essa hora pra ser 18:05

#if (horaEntrada == 17 and minutosEntrada == 65): # se for a hora for 17:65 se tornará 18:05
 #   horaEntrada = 18;
 #   minutosEntrada = 5;
#  print("A hora de saída é: ", horaEntrada, "e", minutosEntrada, "minutos.")
    
#if (minutosEntrada > 60):
 #   horaEntrada + 1;
  #  minutosEntrada - 60;
   # print("A hora de saída é: ", horaEntrada, "e", minutosEntrada, "minutos.")