# Definindo uma pontuação para o usuário 

import random

print("*********************************")
print("Bem vindo ao jogo de adivinhação!")
print("*********************************")

numero_secreto = random.randrange(1,101)
total_de_tentativas = 0
pontos = 1000

print("Qual nível de dificuldade?")
print("(1)\t Fácil\n(2)\t Médio\n(3)\t Dificíl")

nivel = int(input("Defina um nível: "))
# Professor da FIAP disse que se for só um código, pode ser na mesma linha do if/else e funcionou! :)
if(nivel == 1): total_de_tentativas = 20
elif(nivel == 2): total_de_tentativas = 10
else: total_de_tentativas = 5


for rodada in range(1, total_de_tentativas + 1) :
    
    print(f"Tentativa {rodada} de {total_de_tentativas}")
    chute_str = input(" Digite o seu número entre 1 e 100: ")
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
        print(f"Você acertou e fez {pontos} pontos!")
        break
    # Break não seria o ideal, mas deu certo e por enquanto só sei assim :) {No fim o professor do curso usou o break rssss}
    else:
        if (maior):
            print("Você errou! O seu chute foi maior que o número secreto.")
        elif (menor):
            print("Você errou! O seu chute foi menor que o número secreto.")
        pontos_perdidos = abs(numero_secreto - chute)
        pontos = pontos - pontos_perdidos

print(f"A resposta correta é {numero_secreto}\nFim do jogo")