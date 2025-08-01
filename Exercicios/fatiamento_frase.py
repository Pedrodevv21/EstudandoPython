#fatiamento de frase 

frase = (input ("digite uma frase: "))

if frase:
    print (f"5 primeiras letras: {frase[0:5]}")
    print (f"ultimos 5 :{frase[-5:]}")
    print (f"posiçoes impares: {frase[::2]}")
    print (f"posiçoes impares: {frase[1::2]}")
    print (f"frase invertida: {frase[::-1]}")
else: 
    print ("voçe não digitou nenhuma frase")
