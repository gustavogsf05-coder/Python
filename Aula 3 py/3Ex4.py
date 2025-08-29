salario = float(input ("Digite seu salario: ") )

if  salario > 1250:
    salario1 = salario*1.1
    print(f"Seu salario com aumento é: {salario1:.2f} ")
elif  salario <= 1250 :
    salario2= salario*1.15
    print(f"Seu salario com aumento é: {salario2:.2f} ")