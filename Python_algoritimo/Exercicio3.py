dias = int(input("digite a quantidade de dias: "))
h = int(input("digite a quantidade de horas: "))
min = int(input("digite a quantidade de minutos: "))
sec = int(input("digite a quantidade de segundos: "))

totalsec = (dias * 86400) + (h * 3600) + (min*60) + sec

print(f"o total de segundos foi: {totalsec:.2f}")