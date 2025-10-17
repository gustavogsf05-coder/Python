# M = []

# for num_linha in range(10):
#     linha = []
#     for num_coluna in range(15):
#         linha.append(num_linha + num_coluna)

#     M.append(linha)

# for linha in range(len(M)):
#     for coluna in range(len(M[linha])):
#         print("%4d" % M[linha][coluna], end=" ")
#     print()


# #Ex1

# from random import randint

# M = []

# for num_linha in range(10):
#     linha = []
#     for num_coluna in range(15):
#         linha.append(randint(0, 100))

#     M.append(linha)

# for linha in range(len(M)):
#     for coluna in range(len(M[linha])):
#         print("%4d" % M[linha][coluna], end=" ")
#     print()

# print("----------------------------------")
# for linha in range(len(M)):
#     print(M[linha][0])



from random import randint  # Importa a função randint

M = []

def gerar_matriz(num_linha, num_coluna):
    for i in range(num_linha):         
        linha = []
        for j in range(num_coluna):    
            linha.append(randint(0, 100))
        M.append(linha)

gerar_matriz(10, 15)

for linha in M:
    print(linha)

for linha in range(len(M)):
    for coluna in range(len(M[linha])):
        print("%4d" % M[linha][coluna], end=" ")
    print()

print("----------------------------------")
for linha in range(len(M)):
    print(M[linha][0])

#Ex3



