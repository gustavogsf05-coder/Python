# nn = int(input("digite quantos numeros serão verificados: "))

# num = int(input("Digite um numeno inteiro: "))
# eh_primo = True

# for i in range(nn):
#     for i in range (2,num):
#         if num % i == 0:
#             eh_primo = False
#             # break

# if eh_primo and num >1:
#     num = num + 1 
#  #print(f"{num} é primo")

# #else:
# #    print("não é primo")
    



# Solicita o número de entradas
nn = int(input("Digite quantos números serão verificados: "))

# Variável para contar quantos números primos foram encontrados
quantidade_primos = 0

# Loop para verificar cada número
for _ in range(nn):
    num = int(input("Digite um número inteiro: "))
    eh_primo = True  # Assumir que o número é primo inicialmente

    # Verificar se o número é primo
    if num > 1:
        for i in range(2, num):
            if num % i == 0:
                eh_primo = False
                break  # Não precisa continuar verificando se o número não for primo
    else:
        eh_primo = False  # Números menores ou iguais a 1 não são primos

    # Se o número for primo, incrementa o contador
    if eh_primo:
        quantidade_primos += 1

# Exibe o resultado final
print(f"Quantidade de números primos: {quantidade_primos}")