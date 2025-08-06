senha = (input ("digite uma senha forte: "))

if senha:
    if len (senha) > 8:
        print ("sua senha tem mais de 8 caracteres")
    if "A" in senha:
        print ("sua senha tem a letra A maiúscula")
    if "@" in senha:
        print ("sua senha tem @")
    if "7" in senha:
        print ("sua senha tem o numero 7")
    else:
        print ("sua senha esta invalida")
else:
    print ("Preencha os campos vazios")



         