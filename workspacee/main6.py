# Pedi pro chat me dar um exercicio pra mim fazer e ele me deu:
# Calculadora de desconto progessivo

Valor_compra =float (input("Qual o valor da minha compra"'? '))
if Valor_compra <=100:
    taxa_desconto = 5
elif 101 <= Valor_compra <=300:
    taxa_desconto = 10
else:
     taxa_desconto = 15

valor_final = Valor_compra - (Valor_compra * taxa_desconto /100)
print(f"valor total da minha conta {valor_final:.2f}" )