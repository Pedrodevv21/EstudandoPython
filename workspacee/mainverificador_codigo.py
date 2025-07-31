'''
exercicio
'''
#verificador de codigo 

codigo = input ("me fale um codigo:")

if len (codigo) > 0:
    if len (codigo) >=8:
        print ("esse codigo tem 8 caracteres")
    else:    
         print ("não tem 8 caracteres")
    
    if codigo [0]=="A":
            print ("esse codigo começa com a letra certa")
    else:
             
             print ("não começa com a letra certa")
    if "7" in codigo:
                print ("contém o numero certo")
    else:
      
                print ('não contem o numero certo')
    if " " not in codigo:
                 print ('não tem espaço')
else:
    print("voçe deixou campos vazios")