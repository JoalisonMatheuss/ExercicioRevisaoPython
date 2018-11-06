print("Qual tipo de carne você deseja comprar?\n")
print("Digite 1 para comprar File Duplo.")
print("Digite 2 para comprar Alcatra.")
print("Digite 3 para comprar Picanha.\n")


compra = int(input("Tipo da carne: "))
peso = float(input("O peso da carne vai ser: "))

tipoCarne = ""

if compra == 1:
  tipoCarne = "File Duplo"

elif compra == 2:
  tipoCarne = "Alcatra"

elif compra == 3:
  tipoCarne = "Picanha"

desconto = 0
compraRealizada = 0

pagamento = str(input("Deseja comprar no cartao Tabajara? "))
print("")
pagamento = pagamento.upper()

file_duplo = 0
alcatra = 0
picanha = 0

if compra == 1 and peso<=5:
  file_duplo = float(int(peso)*4.9)

elif compra == 1 and peso>5:
  file_duplo = float(int(peso)*5.8)

elif compra == 2 and peso<=5:
  alcatra = float(int(peso)*5.9)

elif compra == 3 and peso>5:
  alcatra = float(int(peso)*6.8)

elif compra == 3 and peso<=5:
  picanha = float(int(peso)*6.9)

elif compra == 3 and peso>5:
  picanha = float(int(peso)*7.8)

if file_duplo > 0:
  compraRealizada = file_duplo

elif alcatra > 0:
  compraRealizada = alcatra

elif picanha > 0:
  compraRealizada = picanha


forma_pagamento = " "
if pagamento == "SIM":
  desconto = float(0.05*compraRealizada)
  forma_pagamento = "Cartao Tabajara"

else:
  forma_pagamento = "A vista"

print("O tipo de carne é: %s."%(tipoCarne
                                ))
print("O quantidade de carne é: %.2f kg"%(peso))
print("O preco total é: R$ %.2f"%(compraRealizada))
print("A forma de pagamento é: %s"%(forma_pagamento))
print("O valor do desconto é: R$ %.2f"%(desconto))
print("O valor total a pagar é: R$ %.2f"%(compraRealizada-desconto))
