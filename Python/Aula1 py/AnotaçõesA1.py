#print("Ola, mundo")
#clear ou cls para limpar terminal
#ls para visualizar os arquivos
#cd ..(vai para pasta anterior)
#cd . (pasta atual)
#type mostra o tipo de dado


print("hello word!")

print(type(3.6))
print(type(2))

print(type("ola"))
print(type("2.8"))

print(type(2+6j))

a= 5
b= 6
mult= a*b


#forma de mostrar vairiaveis
print(a+b)
print(mult)
#primeira forma
print("a vale",a)
#segunda forma
print("a vale %d"%a)
#terceira forma
print("a vale {0}".format(a))
#quarta forma
print(f"a vale {a}")

print(f"a vale {a:.1f}")


#pelé
#coletando dados

nome = input("Digite seu nome:")
print(f"nome digitado:{nome}")