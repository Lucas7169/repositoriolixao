num1 = int(input("Digite um número:"))
num2 = int(input("Digite mais um número:"))
num3 = int(input("Digite mais um número:"))

if (num1 + num2)>num3:
    print("é um triangulo")
    if num1 == num2 and num1 == num3:
        print("O triangulo é Equilátero")
    elif num1 == num2 and num1 != num3:
        print("O triangulo é isósceles")
    elif num1 != num2 and num1 != num3:
        print("O trinangulo é Escaleno")
