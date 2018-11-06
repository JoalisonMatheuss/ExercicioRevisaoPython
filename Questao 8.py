lista = []
i = 1
media = 0 
soma = 0

while True:
    notas = float(input("Digite o %s elemento:"%(i)))
    if notas == -1:
        break
    soma+=notas
    lista.append(notas)
    i+=1

print("A) Número de elementos digitados: %s \n"%(i))    
print("B) Números um ao lado do outro: \n",lista)

contador = len(lista)-1
print("C) Elementos ao contrario:")
while contador >= 0:
    print(lista[contador])
    contador-=1

print("D) A soma dos elementos é: %.1f \n"%(soma))
print("E) A media dos valores é: %.1f \n"%(soma/len(lista)))

AcimaMedia = 0
for l in range(len(lista)):
  if lista[l] > soma/len(lista):
    AcimaMedia +=1
print("F) Quantidade de valores acima da média é: %s \n"%(AcimaMedia))

AbaixoDaNota = 0 
for abaixo in range(len(lista)):
    if lista[abaixo] < 7:
        AbaixoDaNota+=1

print("G) Quantidade de elementos abaixo da média: %d \n"%(AbaixoDaNota))

print("H) Tá osso, Tá tenso")

    
