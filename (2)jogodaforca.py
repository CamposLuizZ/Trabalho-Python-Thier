import random

def escolher_palavra():
    palavras = ["DESENVOLVIMENTO", "TECNOLOGIA", "LOGICA", "PROGRAMACAO", "TENDENCIAS"]
    return random.choice(palavras)

# Teste da função escolher_palavra
palavra_aleatoria = escolher_palavra()
print("Palavra escolhida:", palavra_aleatoria)

def exibir_forca(tentativas):
    fases_forca = [
        """
           ___
          |       |
                  |
                  |
                  |
                  |
        ___| 
        """,
        """
           ___
          |       |
          O       |
                  |
                  |
                  |
        ___| 
        """,
        """
           ___
          |       |
          O       |
          |       |
                  |
                  |
        ___| 
        """,
        """
           ___
          |       |
          O       |
         /|       |
                  |
                  |
        ___| 
        """,
        """
           ___
          |       |
          O       |
         /|\      |
                  |
                  |
        ___| 
        """,
        """
           ___
          |       |
          O       |
         /|\      |
         /        |
                  |
        ___| 
        """,
        """
           ___
          |       |
          O       |
         /|\      |
         / \      |
                  |
        ___| 
        """
    ]
    
    print(fases_forca[tentativas])

# Teste da função exibir_forca
exibir_forca(3)

def jogar():
    palavra = escolher_palavra()
    palavra_oculta = ['_'] * len(palavra)
    letras_tentadas = []
    tentativas = 0

    print("Bem-vindo ao Jogo da Forca!")
    print("Adivinhe a palavra oculta.")

    while tentativas < 6:
        letra = input("Digite uma letra: ").upper()

        if letra in letras_tentadas:
            print("Você já tentou esta letra. Tente outra.")
            continue

        letras_tentadas.append(letra)

        if letra in palavra:
            for i in range(len(palavra)):
                if palavra[i] == letra:
                    palavra_oculta[i] = letra
        else:
            tentativas += 1

        print("Palavra: ", " ".join(palavra_oculta))
        print("Letras tentadas:", " ".join(letras_tentadas))
        exibir_forca(tentativas)

        if '_' not in palavra_oculta:
            print("Parabéns! Você adivinhou a palavra correta:", palavra)
            break

    if '_' in palavra_oculta:
        print("Você foi enforcado! A palavra correta era:", palavra)

# Teste da função jogar
jogar()

def jogar():
    palavra = escolher_palavra()
    palavra_oculta = ['_'] * len(palavra)
    letras_tentadas = []
    tentativas = 0

    print("Bem-vindo ao Jogo da Forca!")
    print("Adivinhe a palavra oculta.")

    while tentativas < 6:
        letra = input("Digite uma letra: ").upper()

        if letra in letras_tentadas:
            print("Você já tentou esta letra. Tente outra.")
            continue

        letras_tentadas.append(letra)

        if letra in palavra:
            for i in range(len(palavra)):
                if palavra[i] == letra:
                    palavra_oculta[i] = letra
        else:
            tentativas += 1

        print("Palavra: ", " ".join(palavra_oculta))
        print("Letras tentadas:", " ".join(letras_tentadas))
        exibir_forca(tentativas)

        if '_' not in palavra_oculta:
            print("Parabéns! Você adivinhou a palavra correta:", palavra)
            break

    if '_' in palavra_oculta:
        print("Você foi enforcado! A palavra correta era:", palavra)

# Teste da função jogar
jogar()