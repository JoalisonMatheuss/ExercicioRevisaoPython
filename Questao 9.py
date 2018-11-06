veiculos = []
consumo = []
litros_10km = []
consumo10km = 0
precos = []
precoGasolina = 0

for i in range(1,6):
  veiculo1 = str(input("Informe o veiculo %d: "%(i)))
  consumo1 = float(input("Informe o consumo do veiculo %d: "%(i)))
  print("")

  veiculos.append(veiculo1)
  consumo.append(consumo1)

  consumo10km = float(1000/consumo1)
  litros_10km.append(consumo10km)

  precoGasolina = float(consumo10km*3.5)
  precos.append(precoGasolina)


print("Modelo   KM/L    1000KM     PREÇO")
for i in range(5):
  print("%s - %.1f - %.1f litros - R$ %.2f" %(veiculos[i], consumo[i], litros_10km[i], precos[i]))

print("")

MenorConsumo = min(litros_10km)

ConsumoCarro = 0

MelhorConsumo = 0

for j in range(len(litros_10km)):
  ConsumoCarro = litros_10km[i] 

  if ConsumoCarro == MenorConsumo:
    MelhorConsumo = i

print("O menor consumo é do %s"%(veiculos[MelhorConsumo]))
