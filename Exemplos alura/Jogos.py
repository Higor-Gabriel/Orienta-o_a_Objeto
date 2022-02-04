import Adivinhacao
import Forca

def escolher_jogo():

    print("*********************************")
    print("      Escolha o seu Jogo")
    print("*********************************")

    print("(1) Adivinhação (2) Forca")

    jogo = int(input("Qual Jogo pretende Jogar ?"))

    if jogo == 1:
        print("Jogando Adivinhação")
        Adivinhacao.jogar_adivinhacao()
    elif jogo == 2:
        print("jogando Forca")
        Forca.jogar_forca()


if __name__ == "__main__":
    escolher_jogo()