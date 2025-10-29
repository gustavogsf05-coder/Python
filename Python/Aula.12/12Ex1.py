
#Escreve no banco de dados

# arquivo = open ("teste.txt", "w")

# for linha in range (1, 101) :
#     arquivo.write ("Linha %d\n" % linha)

# arquivo.close ()

#Mostra o conteudo do banco de dados

# arquivo = open ("teste.txt", "r")

# for linha in arquivo.readlines () :
#     print (linha)
#     print (linha.strip())
# arquivo. close ()

#exemplo 1  onde contamos de 0 a 999, nele temos que gerar separar em dois arquivos os numeros impares e pares, imprime a qantidade de numeros de cada lado.

#primeiro jeito

# pares = open("pares.txt","w")
# impares = open("impares.txt","w")

# for numero in range(100):
#     if numero % 2 == 0:
#         pares.write(f"{numero}\n")
#     else:
#         impares.write(f"{numero}\n")
        
# pares.close()
# impares.close()

#segundo projeto

# with open('pares.txt','w') as pares, open('impares.txt','w') as impares:
#     for numero in range(100):
#         if numero % 2 == 0:
#             pares.write(f"{numero}\n")
#         else:
#             impares.write(f"{numero}\n")

# Ex2

# with open ('pares','r') as pares, open ('multiplos','w')as multipos: 
#     for linha in pares.readline():
#         valor = int(linha.strop())
#         if valor % 4==0:
#             multipos.write(linha)
    


#manipulando o print
#


#Ex3

#Meu


# with open ('contatos.txt',"w")as contatos:
#     while True:
#         nome = input("Digite seu nome: ")
#         telefone =input("Digite seu numero de telefone: ")
#         if nome =="" and telefone =='':
#             break
#         with open("contatos.txt","a") as contatos:
#             contatos.write(f"{nome},{telefone}\n")
# with open ("contatos.txt","r") as contatos:
#     for linha in contatos:
#         nome,telefone = linha.strip().split(",")
#         print(f"Nome: {nome:25} - Telefone: {telefone}")


#Chat

# # Abre o arquivo em modo de escrita (substitui o conteúdo anterior)
# with open('contatos.txt', 'w') as contatos:
#     while True:
#         nome = input("Digite seu nome: ")
#         telefone = input("Digite seu número de telefone: ")

#         if not nome and not telefone:
#             break

#         contatos.write(f"{nome},{telefone}\n")

# # Lê o arquivo e mostra os contatos
# with open('contatos.txt', 'r') as contatos:
#     for linha in contatos:
#         nome, telefone = linha.strip().split(",")
#         print(f"Nome: {nome:25} - Telefone: {telefone}")
