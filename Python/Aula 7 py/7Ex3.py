def maximo(x, y):
    """
    calcula o maior numero de dosi numeros
    """   
    if x>y:
        return(x)
    else:
        return(y)

num1 = int(input("numero 1: "))
num2 = int(input("numero 2: "))

resultado = maximo(num1,num2)

print(f"o maior valor é:{resultado} ")



