
nota1 = float(input("Digite a primeira nota: "))
nota2 = float(input("Digite a segunda nota: "))
nota3 = float(input("Digite a terceira nota"))
nota4 = float(input("Digite a Quarta nota: "))

media = (nota1+nota2+nota3+nota4)/4

if media >= 7:
    print("Notas do aluno: %.1f, %.1f, %.1f, %.1f"%(nota1, nota2, nota3, nota4))
    print("A media do aluno é %.1f, ele foi aprovado"%(media))
else:
    print("A media do aluno é %.1f, ele foi reprovado"%(media))

