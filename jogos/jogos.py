
print("*********************************")
print("*******Escolha o seu jogo********")
print("*********************************")

print("(1)\t forca\n(2)\t advinhação")

jogo = int(input("Qual jogo?\n"))

if(jogo == 1):
    print("\n...Jogando forca...\n")
    import ex1
elif(jogo == 2):
    print("\n...Jogando Advinhação...\n")
    import ex7
else :
    print("Escolha uma das Opções")
