# O laço com for (in range) {Transformando do while para o for!}

print("*********************************")
print("Bem vindo ao jogo de adivinhação!")
print("*********************************")

numero_secreto = 42
total_de_tentativas = 3
rodada = 1

for rodada in range(1, total_de_tentativas + 1) :
    
    print(f"Tentativa {rodada} de {total_de_tentativas}")
    chute_str = input("Digite o seu número entre 1 e 100: ")
    print(f"Você digitou: {chute_str}")
    chute = int(chute_str)   

    if(chute <  1 or chute > 100):
        print("Você deve digitar um número ente 1 e 100!")
        continue 
    # continue tipo o break mas continua

    acertou = numero_secreto == chute
    maior = chute > numero_secreto
    menor = chute < numero_secreto

    if(acertou):
        print("Você acertou!")
        break
    # Break não seria o ideal, mas deu certo e por enquanto só sei assim :) {No fim o professor do curso usou o break rssss}
    else:
        if (maior):
            print("Você errou! O seu chute foi maior que o número secreto.")
        elif (menor):
            print("Você errou! O seu chute foi menor que o número secreto.")

    rodada = rodada + 1

print("Fim do jogo")