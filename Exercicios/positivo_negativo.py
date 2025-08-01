# verificador de código impar ou par positivo/negativo

numero_inteiro = int(input("Digite um número inteiro: ")) 

if numero_inteiro == 0:
    print ("zero é neutro")
elif numero_inteiro % 2 == 0 and numero_inteiro > 0:
    print ("esse numero é par positivo") 
elif numero_inteiro % 2 == 0 and numero_inteiro < 0:
   print("esse numero é par negativo")
elif numero_inteiro % 2 != 0 and numero_inteiro > 0:
    print ("esse numero é impar positivo")
elif numero_inteiro % 2 != 0 and numero_inteiro < 0:
    print ("esse numero é impar negativo")
else:
    ...

    