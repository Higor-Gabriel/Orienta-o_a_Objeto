import random


def jogar_forca():

    abertura_jogo()
    palavra_secreta = carregar_palavra_secreta()
    letras_certas = inicializa_letras_certas(palavra_secreta)

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


def inicializa_letras_certas(palavra):
        return ["_" for letra in palavra]

def abertura_jogo():
        print("*********************************")
        print("Bem vindo ao jogo de Forca")
        print("*********************************")

def carregar_palavra_secreta():

        arquivo = open("palavras.txt", "r")
        palavras = []

        for linha in arquivo:
            linha = linha.strip()
            palavras.append(linha)

        arquivo.close()

        numero = random.randrange(0, len(palavras))
        palavra_secreta = palavras[numero].upper()
        return palavra_secreta

if __name__ == "__main__":
    jogar_forca()