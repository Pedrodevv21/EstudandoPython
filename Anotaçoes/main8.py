#qual o maior numero ?

Primeiro_valor = int (input ("digite o primeiro valor:"))
Segundo_valor = int (input ("digite o segundo valor:"))
Terceiro_valor = int (input ("digite o terceiro valor:"))

if Primeiro_valor > Segundo_valor and Primeiro_valor > Terceiro_valor:
    print ("maior valor e o primeiro")
elif Segundo_valor > Terceiro_valor and Segundo_valor > Primeiro_valor:
    print ("maior valor e o segundo") 
elif Terceiro_valor > Primeiro_valor and Terceiro_valor > Segundo_valor:
    print ("maior valor e o terceiro") 
elif Primeiro_valor == Segundo_valor and Primeiro_valor > Terceiro_valor:
    print ("os primeiro e o segundo valor são iguais")
elif Segundo_valor == Terceiro_valor and Segundo_valor > Primeiro_valor:
    print ("o segundo e o terceiro valor são iguais")
else:
    print ("os valores são iguais")
