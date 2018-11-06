lista1 = []
lista2 = []
i = 0
j = 0
m = 0 
while i < 10:
    a = int(input("Digite o %s elemento da primeira lista: "%(i+1)))
    lista1.append(a)
    i+=1
print("-------------------------------------------------------------")
while j < 10:
    b = int(input("Digite o %s elemento da segunda lista: "%(j+1)))
    lista2.append(b)
    j+=1
print("-------------------------------------------------------------")
vetor = []

for i in range(10):
    a = lista1[i]
    b = lista2[i]
    vetor.append(a)
    vetor.append(b)

print(vetor)
