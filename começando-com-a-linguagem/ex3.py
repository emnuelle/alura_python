# O laço com o while; para repetir o jogo enquanto o usuario nâo acerta o numero/Adicionando tentativas
# Testando a condição elif
# Usando também a função format 'f{}'
print("*********************************")
print("Bem vindo ao jogo de adivinhação!")
print("*********************************")

numero_secreto = 42
total_de_tentativas = 3
rodada = 1

while (rodada <= total_de_tentativas):
    
    print(f"Tentativa {rodada} de {total_de_tentativas}")
    chute_str = input("Digite o seu número: ")
    print(f"Você digitou: {chute_str}")
    chute = int(chute_str)   

    acertou = numero_secreto == chute
    maior = chute > numero_secreto
    menor = chute < numero_secreto

    if (acertou):
        print("Você acertou!")
        break
    # Break não seria o ideal, mas deu certo e por enquanto só sei assim :) 
    else:
        if (maior):
            print("Você errou! O seu chute foi maior que o número secreto.")
        elif (menor):
            print("Você errou! O seu chute foi menor que o número secreto.")

    rodada = rodada + 1

print("Fim do jogo")