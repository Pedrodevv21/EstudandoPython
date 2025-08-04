
try:
    num1 = float (input ("digite um numero: "))
    num2 = float (input ("digite o segundo numero: "))

    resultado = num1 / num2
    print (f"O resultado dos dois números é: ", resultado)
except:
    print ("ocorreu um erro, verifique se digitou os números validos e se não dividiu por zero")


