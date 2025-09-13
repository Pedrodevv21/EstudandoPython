while True:
    numero_1 = (input ("Digite um numero: "))
    numero_2 = (input ("Digite segundo o numero: "))
    operador = (input ("digite o operador (+-*/): "))
   
    numeros_validos = None

    try:
        numero_1_float = float (numero_1)
        numero_2_float = float (numero_2)
        numeros_validos = True
    except:
        numeros_validos = None

    if numeros_validos is None:
        print ("Um ou ambos os números digitados são invalidos")
        continue

        
    operadores_permitidos =  "+-*/"

    if operador not in operadores_permitidos:
        print('operador invalido')

    if len (operador) > 1:
        print ("Digite apenas um operador") 

    if operador == "+":
        resultado_soma = int (numero_1_float + numero_2_float)
        print (f"A soma dos números é: {resultado_soma}")
    elif operador == "-":
        resultado_subtraçao = int (numero_1_float - numero_2_float)
        print (f"A subtraçao dos números é: {resultado_subtraçao}")
    elif operador == "*":
        resultado_mulplicaçao = int (numero_1_float * numero_2_float)
        print (f"A mulplicaçao dos números é: {resultado_mulplicaçao}")
    elif operador == "/":
        resultado_divisão = int (numero_1_float / numero_2_float)
        print (f"A divisão dos números é: {resultado_divisão}")
    else:
        ...
    

    sair = input ("Quer sair ? ")
    if sair == "sim":
        print ("Voçe saiu")
        break