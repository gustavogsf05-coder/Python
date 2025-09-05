preco = float(input("digite o valor do produto: "))
id_p = int(input("digite o id do produto: "))

if id_p ==1:
    procedencia = "sul"
elif id_p ==2:
    procedencia = "Norte"
elif  id_p ==3:
    procedencia = "Leste"
elif  id_p ==4:
    procedencia = "Oeste"
elif  id_p ==5 or id_p ==6:
    procedencia = "Nordeste"
elif id_p ==7 or id_p == 8 or id_p ==9:
    procedencia = "Sudeste"
elif id_p >=10 and id_p <=20:
    procedencia = "Centro-Oeste"
elif id_p >=25 and id_p <=30:
    procedencia = "Nordeste"
else:
    print("produto importado")

print(f"produto procedente da região {procedencia} o valor é {preco}")