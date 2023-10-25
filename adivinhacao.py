import random
import os


def jogar():
    print("****************************************")
    print("*** Bem vindo ao Jogo de Adivinhação ***")
    print("****************************************")

    numero_secreto = random.randrange(1, 101)
    total_de_tentativas = 0
    pontos = 1000

    print("Qual o nível de dificuldade?")
    print("(1) Fácil\n(2) Médio\n(3) Difícil")

    nivel = int(input("Escolha o nível: "))

    if nivel == 1:
        total_de_tentativas = 20
    elif nivel == 2:
        total_de_tentativas = 10
    elif nivel == 3:
        total_de_tentativas = 5
    else:
        print("Nível escolhido inválido")

    # while (rodada <= total_de_tentativas):
    for rodada in range(1, total_de_tentativas + 1):

        print("Tentativa {} de {}".format(rodada, total_de_tentativas))

        chute = int(input("Digite um número entre 1 e 100: "))

        os.system('cls')

        print("Você digitou {}".format(chute))

        if (chute < 1 or chute > 100):
            print("Você deve digitar um número entre 1 e 100!")
            continue

        acertou = chute == numero_secreto
        maior = chute > numero_secreto
        menor = chute < numero_secreto

        if (acertou):
            print("Você acertou!!! O número secreto era {} e você fez {} pontos!".format(
                numero_secreto, pontos))
            break
        else:
            if (maior):
                print(
                    "Você errou! O seu chute ({}) foi maior que o número secreto.".format(chute))
            elif (menor):
                print(
                    "Você errou! O seu chute ({}) foi menor que o número secreto.".format(chute))

            pontos_perdidos = abs(numero_secreto - chute)
            pontos -= pontos_perdidos

    print("Fim do Jogo")


if (__name__ == "__main__"):
    jogar()
