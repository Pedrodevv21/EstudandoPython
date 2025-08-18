'''
horas com bom dia, boa tarde e boa noite
'''

horas_inteiros = int (input ("Que horas são ? "))

if horas_inteiros >= 0 and horas_inteiros <= 11:
    print ("Bom dia!")
elif horas_inteiros >= 12 and horas_inteiros <= 17:
    print ("Boa tarde!")
elif horas_inteiros >= 18 and horas_inteiros <= 23:
    print ("Boa noite!")
else:
    print ("Não conheço essa hora")
    