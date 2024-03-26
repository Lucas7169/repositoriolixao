horas = float(input("Digite quanto voce guanha por hora trabalhada:"))
horas_traba = float(input("Digite as horas trabalhadas no més:"))
salarioB = horas*horas_traba   

inss = 0.08*salarioB
impostoR = 0.11*salarioB
sindicato = 0.05*salarioB
print("O seu salario bruto é:",salarioB)
print("o inss roba:",inss)
print("O imposto de renda desconta do seu salario:",impostoR)
print("O sidicato desconta do seu salario:",sindicato)

salarioL = salarioB-(inss + impostoR + sindicato)
print("O seu salario apos ser roubado do governo é:",salarioL)