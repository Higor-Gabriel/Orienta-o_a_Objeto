
def jogar_forca():
    print("*********************************")
    print("Bem vindo ao jogo de Forca")
    print("*********************************")

    palavra_secretea = "banana"

    enforcou = False
    acertou = False

    while not enforcou and not acertou:

        chute = input("Qual a letra ?")
        index = 0
        for letra in palavra_secretea:
            if chute == letra:
                print("Encontrei a letra {} na posição {}".format(letra, index))
            index = index + 1

        print("Jogando...")
    print("*** FIM DO JOGO ***")

if __name__ == "__main__":
    jogar_forca()