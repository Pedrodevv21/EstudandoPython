
'''
exercício número secreto

'''

numero_secreto = 20

while True:
    chute = int (input ("adivinhe o numero: "))
    if chute == numero_secreto:
        print ("Você acertou o numero secreto")
        break
    else:
        print ("Você errou o numero ou não digitou nenhum numero")
  


