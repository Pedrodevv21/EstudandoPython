#Sistema de cadastro com email e confirmação de senha 

nome = (input ('digite seu nome:'))
email = (input ("digite seu email:"))
senha = (input ("digite sua senha:"))
confirme_senha = (input ("confirme sua senha:"))

if nome and email and senha and confirme_senha:
    if "@" in email and "." in email:
        print ("sim contém @ e .")
    else:
        print ("email esta errado")

    if len (senha) == 6:
        print (f"sim a {senha} tem 6 dígitos")
    else:
        print ("senha esta errada")

    if senha == confirme_senha:
        print ("sim a senha esta certa")
    else:
        print ("a confirmação esta errada")
else:
    print("preencha os campos vazios")






