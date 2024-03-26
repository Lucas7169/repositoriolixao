nota1 = int(input("digite uma nota:"))
nota2 = int(input("digite mais uma nota:"))

resposta = (nota1 + nota2) / 2

if (resposta >= 7 ):
    print("Aprovado")
else:
    print("Reprovado")
if(nota1 == 10 or nota2 == 10 and resposta >= 7):
    print("Aprovado com distintao")

