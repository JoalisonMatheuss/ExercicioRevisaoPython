a = float(input())
b = float(input())
c = float(input())
media = (a+b+c)/3

if media >= 7:
  print("Aprovado")
  print("A media �: %.1f"%(media))
elif media < 7:
  print("Reprovado")
  print("A media �: %.1f"%(media))
elif media == 10:
  print("Aprovado com Distin��o")
  print("A media �: %.1f"%(media))
