
# Ex1 ✓
# lista = []

# for i in range(5):
#     n = int(input("digite um numero"))
#     lista.append(n)

# print(f"a lista completa é {lista}")
# print(f"a lista completa é {lista[0]}")
# print(f"a lista completa é {lista[4]}")

# Ex2 ✓
# t = [11, 7, 2, 4]
# menor = t[0]
# for elemento in t:
#     if elemento<menor:
#         menor = elemento

# print(f"menor elemento é {menor}")

#Ex3

lista  = []

for i in range(10):
    n = int(input("Digite um numero: "))
    lista.append(n)

maior = lista[0]

for numero in lista:
    if numero > maior:
        maior = numero

# print(f"O maior número é:{maior}")
# for indice in range(len(lista)):
#     if lista[indice]>maior
