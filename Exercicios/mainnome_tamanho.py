'''
exercício
'''
#verificador de nome curto médio ou longo

nome = str(input("me fale um nome:"))

if len (nome) <=4:
    print ("esse nome é curto")
elif len(nome) <= 6:
    print ("esse nome é médio")
else:
    print ("esse nome é longo")