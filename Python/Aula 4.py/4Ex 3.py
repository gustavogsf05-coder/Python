sexo = input("Digite seu sexo (M/F): ")
altura = float(input("Digite sua altura(em metros): "))

if sexo == "M":
    ideal = (72.7 * altura) - 58
    print(f"seu peso ideal é {ideal}")

elif sexo == "F":
    ideal = (62.1 * h) - 44.7
    print(f"seu peso ideal é {ideal:.2f}")
else:
    print("sexo invalido digite M(maisuculo caso masculino) F (Maiusculo caso feminino) ")