
def jogar_forca():
    print("*********************************")
    print("Bem vindo ao jogo de Forca")
    print("*********************************")

    palavra_secreta = "maça".upper()
    letras_certas = ["_" for letra in palavra_secreta]

    enforcou = False
    acertou = False
    erros = 0

    print(letras_certas)

    while not enforcou and not acertou:

        chute = input("Qual a letra? ")
        chute = chute.strip().upper()
        if chute in palavra_secreta:
            index = 0
            for letra in palavra_secreta:
                if chute == letra:
                    letras_certas[index] = letra
                index += 1
        else:
            erros +=1

        enforcou = erros == 6
        acertou = "_" not in letras_certas
        print(letras_certas)

    if acertou:
        print("Você ganhou o jogo, Parabéns!")
    else:
        print("Você perdeu!")
    print("*** FIM DO JOGO ***")

if __name__ == "__main__":


    jogar_forca()