print("Bem vindo ao Jogo de adivinhação!")

numero_secreto = 42
total_de_tentativas = 5
rodada = 1
for rodada in range(1, total_de_tentativas + 1):
    print("tentativa: {} de {}". format(rodada, total_de_tentativas))
    chute_str = input("digite o número secreto entre 1 e 100:")
    print("Você digitou", chute_str )
    chute = int(chute_str)
    if(chute <1 or chute > 100)
        print("você deve digitar um número entre 1 e 100.")
        continue

    acertou = numero_secreto == chute
    maior = chute > numero_secreto
    menor = chute < numero_secreto

    if (acertou) :
        print("você acertou o número secreto")
        break
    else :
        if(maior):
          print("você errou o número secreto, o número secreto é menor que",chute_str,".")
        elif(menor):
          print("você errou o número secreto, o número secreto é maior que",chute_str,".")


    rodada = rodada +1
print("fim do jogo")

