import random
from unidecode import unidecode


def jogar():
    imprimir_mensagem_abertura()

    palavra_secreta = carrega_palavra_secreta()
    letras_acertadas = inicializa_letras_acertadas(palavra_secreta)
    imprimir_letras_acertadas(letras_acertadas)

    enforcou = False
    acertou = False
    erros = 0

    while (not enforcou and not acertou):
        chute = chutar()

        if (chute in unidecode(palavra_secreta)):

            marcar_letra_acertada(palavra_secreta, letras_acertadas, chute)

        else:
            erros += 1
            imprime_desenho_forca(erros)

        enforcou = erros == 7
        acertou = "_" not in letras_acertadas

        imprimir_letras_acertadas(letras_acertadas)

    if (acertou):
        imprimir_mensagem_vitoria(palavra_secreta)
    else:
        imprimir_mensagem_derrota(palavra_secreta)

    print("Fim do Jogo")


def imprimir_letras_acertadas(letras_acertadas):
    str_letras_acertadas = ""
    for letra in letras_acertadas:
        str_letras_acertadas = str_letras_acertadas + letra + " "
    print("\n" + str_letras_acertadas.strip() + "\n")


def imprimir_mensagem_derrota(palavra_secreta):
    print("Puxa, você foi enforcado!")
    print("A palavra era {}".format(palavra_secreta))
    print("                 uuuuuuu                 ")
    print("             uu$$$$$$$$$$$uu             ")
    print("          uu$$$$$$$$$$$$$$$$$uu          ")
    print("         u$$$$$$$$$$$$$$$$$$$$$u         ")
    print("        u$$$$$$$$$$$$$$$$$$$$$$$u        ")
    print("       u$$$$$$$$$$$$$$$$$$$$$$$$$u       ")
    print("       u$$$$$$$$$$$$$$$$$$$$$$$$$u       ")
    print("       u$$$$$$'   '$$$'   '$$$$$$u       ")
    print("       '$$$$'      u$u       $$$$'       ")
    print("        $$$u       u$u       u$$$        ")
    print("        $$$u      u$$$u      u$$$        ")
    print("         '$$$$uu$$$   $$$uu$$$$'         ")
    print("          '$$$$$$$'   '$$$$$$$'          ")
    print("            u$$$$$$$u$$$$$$$u            ")
    print("             u$'$'$'$'$'$'$u             ")
    print("  uuu        $$u$ $ $ $ $u$$       uuu   ")
    print(" u$$$$        $$$$$u$u$u$$$       u$$$$  ")
    print("  $$$$$uu      '$$$$$$$$$'     uu$$$$$$  ")
    print("u$$$$$$$$$$$uu    '''''    uuuu$$$$$$$$$$")
    print("$$$$'''$$$$$$$$$$uuu   uu$$$$$$$$$'''$$$'")
    print(" '''      ''$$$$$$$$$$$uu ''$'''         ")
    print("           uuuu ''$$$$$$$$$$uuu          ")
    print("  u$$$uuu$$$$$$$$$uu ''$$$$$$$$$$$uuu$$$ ")
    print("  $$$$$$$$$$''''           ''$$$$$$$$$$$'")
    print("   '$$$$$'                      ''$$$$'' ")
    print("     $$$'                         $$$$'  ")


def imprimir_mensagem_vitoria(palavra_secreta):
    print("Parabéns, você ganhou!")
    print("A palavra era {}".format(palavra_secreta))
    print("       ___________      ")
    print("      '._==_==_=_.'     ")
    print("      .-\\:      /-.    ")
    print("     | (|:.     |) |    ")
    print("      '-|:.     |-'     ")
    print("        \\::.    /      ")
    print("         '::. .'        ")
    print("           ) (          ")
    print("         _.' '._        ")
    print("        '-------'       ")


def imprime_desenho_forca(erros):
    print("  _______     ")
    print(" |/      |    ")

    if (erros == 1):
        print(" |      (_)   ")
        print(" |            ")
        print(" |            ")
        print(" |            ")

    if (erros == 2):
        print(" |      (_)   ")
        print(" |      \     ")
        print(" |            ")
        print(" |            ")

    if (erros == 3):
        print(" |      (_)   ")
        print(" |      \|    ")
        print(" |            ")
        print(" |            ")

    if (erros == 4):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |            ")
        print(" |            ")

    if (erros == 5):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |       |    ")
        print(" |            ")

    if (erros == 6):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |       |    ")
        print(" |      /     ")

    if (erros == 7):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |       |    ")
        print(" |      / \   ")

    print(" |            ")
    print("_|___         ")
    print()


def marcar_letra_acertada(palavra_secreta, letras_acertadas, chute):
    index = 0

    for letra in palavra_secreta:
        if (chute == unidecode(letra)):
            letras_acertadas[index] = letra

        index += 1


def chutar():
    chute = input("Digite uma letra: ")
    chute = unidecode(chute).strip().upper()
    return chute


def inicializa_letras_acertadas(palavra_secreta):
    return ["_" for letra in palavra_secreta]


def carrega_palavra_secreta():
    palavras = []

    with open("palavras.txt", "r") as arquivo:
        for linha in arquivo:
            palavras.append(linha.strip())

    numero = random.randrange(0, len(palavras))
    palavra_secreta = palavras[numero].upper()
    return palavra_secreta


def imprimir_mensagem_abertura():
    print("****************************************")
    print("***    Bem vindo ao Jogo da Forca    ***")
    print("****************************************")


if (__name__ == "__main__"):
    jogar()
