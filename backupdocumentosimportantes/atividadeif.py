nota1 = float(input("Digite a primeira nota:"))
nota2 = float(input("Digite a segunda nota:"))
nota3 = float(input("Digite a terceira nota:"))

notaTotal = (nota1 + nota2 + nota3) /3
if (notaTotal >= 7):
    print("Aprovado")

if (notaTotal and 10 ):
    print("Aprovado com distinção")
else:
    print("Reprovado")

