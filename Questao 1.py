a = float(input())
b = float(input())
c = float(input())
media = (a+b+c)/3

if media >= 7:
  print("Aprovado")
  print("A media é: %.1f"%(media))
elif media < 7:
  print("Reprovado")
  print("A media é: %.1f"%(media))
elif media == 10:
  print("Aprovado com Distinção")
  print("A media é: %.1f"%(media))
