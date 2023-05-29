import advinhacao_completo
import forca


def escolhe_jogo():
    print("*******************************")
    print("******Escolha o seu jogo!******")
    print("*******************************")

    print("(1) Forca (2) Advinhação")

    jogo = int(input("Qual jogo?"))

    if (jogo == 1):
        print("Você escolheu forca")
        forca.jogar()
    if (jogo == 2):
        print("Você escolheu advinhação")
        advinhacao_completo.jogar()


if (__name__ == "__main__"):
    escolhe_jogo()
