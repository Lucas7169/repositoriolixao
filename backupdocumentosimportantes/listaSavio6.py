num1 = int(input("Digite um número:"))
num2 = int(input("Digite mais um número:"))
num3 = int(input("Digite mais um número:"))

if num1 > num2 and num1> num3:
    print("O número maior é",num1)

elif num2 > num1 and num2 > num3:
    print("O número maior é",num2)

elif  num3 > num2 and num3 > num1:
    print("O numero maior é",num3)

if num1 < num2 and num1 < num3:
    print("O número menor é",num1)

elif num2 < num1 and num2 < num3:
    print("O número menor é",num2)

elif  num3 < num2 and num3 < num1:
    print("O numero menor é",num3)
