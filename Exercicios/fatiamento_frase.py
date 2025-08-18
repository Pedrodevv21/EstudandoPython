'''
fatiamento de frase 
'''
frase = (input ("digite uma frase: "))

if frase:
    print (f"5 primeiras letras: {frase[0:5]}")
    print (f"últimos 5 :{frase[-5:]}")
    print (f"posições impares: {frase[::2]}")
    print (f"posições impares: {frase[1::2]}")
    print (f"frase invertida: {frase[::-1]}")
else: 
    print ("você não digitou nenhuma frase")
