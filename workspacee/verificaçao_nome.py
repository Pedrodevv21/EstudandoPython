# CPF Simétrico

cpf =(input ("digite seu seu cpf:"))


if len (cpf) == 11 and cpf.isdigit():
    print (f"o CPF está correto")

    cpf_primeiros = cpf[:3]
    cpf_últimos = cpf [-3:]

    if cpf_primeiros == cpf_últimos:
        print ("o cpf é simétrico")
    else: 
        print ("o CPF não é simétrico")
else:
    print (f"o CPF está incorreto")


