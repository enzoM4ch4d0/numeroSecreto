import random

print('---------------------------------')
print("Bem vindo ao Jogo de adivinhação!")
print('---------------------------------')
numero_secreto = random.randrange(1,101)
total_de_tentativas = 0
pontos = 1000

print("Qual o nível de dificuldade?",)
print("(1)Fácil (2)Médio (3)Difícil")
nivel = int(input("Defina o nível:"))

if( nivel == 1):
    total_de_tentativas = 15
elif(nivel == 2):
    total_de_tentativas = 10
elif(nivel== 3):
    total_de_tentativas = 5

rodada = 1

print(numero_secreto)

for rodada in range(1, total_de_tentativas + 1):
    print("tentativa: {} de {}". format(rodada, total_de_tentativas))
    chute_str = input("digite o número secreto entre 1 e 100:")
    print("Você digitou", chute_str )
    chute = int(chute_str)
    if(chute <1 or chute > 100):
        print("você deve digitar um número entre 1 e 100.")
        continue

    acertou = numero_secreto == chute
    maior = chute > numero_secreto
    menor = chute < numero_secreto

    if (acertou) :
        print("você acertou o número secreto e fez {} pontos".format(pontos))
        break
    else :
        if(maior):
          print("você errou o número secreto, o número secreto é menor que",chute_str,".")
        elif(menor):
          print("você errou o número secreto, o número secreto é maior que",chute_str,".")
        pontos_perdidos = abs(numero_secreto - chute)
        pontos = pontos - pontos_perdidos


    rodada = rodada +1
print("fim do jogo")

