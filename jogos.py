import forca
import adivinhacao


def escolher_jogo():
    print("****************************************")
    print("***         Escolha seu Jogo         ***")
    print("****************************************")

    print("(1) Forca\n(2) Adivinhação")

    jogo = int(input("Escolha o jogo: "))

    if (jogo == 1):
        print("Jogando Forca")
        forca.jogar()
    elif (jogo == 2):
        print("Jogando Adivinhação")
        adivinhacao.jogar()


if (__name__ == "__main__"):
    escolher_jogo()
