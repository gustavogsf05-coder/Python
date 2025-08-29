salario = float(input("digite a quanto você ganha por hora: "))
horas= int(input("digite as horas trabalhadas no mês: "))


salario = salario * horas
imrenda = salario *0.11
inss =  salario *0.08   
sindicato = salario *0.05

sliquido = salario - imrenda - inss - sindicato

print(f"-salario bruto: {salario}")
print(f"-imposto de renda: {imrenda}")
print(f"-inss: {inss}")
print(f"-sindicato: {sindicato}")
print(f"-salario liquido: {sliquido}")

