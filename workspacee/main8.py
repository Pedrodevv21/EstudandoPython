#qual o maior numero ?

Primeiro_valor = int (input ("digite o primeiro valor:"))
Segundo_valor = int (input ("digite o segundo valor:"))
Terceiro_valor = int (input ("digite o terceiro valor:"))

if Primeiro_valor > Segundo_valor and Terceiro_valor:
    print ("maior valor e o primeiro")
elif Segundo_valor > Terceiro_valor and Primeiro_valor:
    print ("maior valor e o segundo") 
elif Terceiro_valor > Primeiro_valor and Segundo_valor:
    print ("maior valor e o terceiro") 
else:
    print ("os valores são iguais")
