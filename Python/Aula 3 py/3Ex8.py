from math import ceil
#tanques = float(input("digite quantos tanques serão pintados: "))
altura = float(input("digite a altura do tanque: "))
raio = float(input("digite agora o raio do tanque(medida): "))
areab = 3.1415*(raio)**2
perimetro = 2*3.1415*raio
areal = altura*perimetro 
areatanq = areab+areal
litros = (areatanq/3)
nlata = ceil(litros/5)
print(f"Área a ser pintada: {areatanq:.2f}")
print(f"quantidade de litros necessarios: {litros:.2f}")
print(f"quantidade de latas: {nlata:.2f}")
if nlata == 1:
    preco = 50
elif nlata == 2:
    preco = 48
elif nlata == 3:
    preco = 46
else: preco = 45
print(f"preço unitario da lata: {preco}")
pctotal = nlata*preco
print(f"custo total: {pctotal:.2f}")