lista = []
while True:
    num = int(input("Digite um numero (negativo para sair) : "))
    if num<0:
        break
lista.append(num)

print(lista)