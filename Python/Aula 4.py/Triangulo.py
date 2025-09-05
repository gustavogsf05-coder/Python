a = int (input ("Lado a: ") )
b = int (input ("Lado b: ") )
c = int (input ("Lado c: ") )
if (a < b + c) and (b < a + c) and (c < a + b) :
    if (a == b) and ( b == c) :
        print ("Tri ngulo equil tero")
    else:
        if (a == b) or (a == c) or (b == c) :
            print ("Triangulo is sceles")
        else:
            print ("Triangulo escaleno")
else:
    print ("Não é Triangulo")