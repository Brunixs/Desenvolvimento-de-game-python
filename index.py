# Imports
import random 
from os import system, name 

# função para limpar a tela a cada execução
def limpa_tela():
    # win
    if name == 'nt':
        _ = system('cls')
    # mac / linux 
    else:
        _ = system('clear')

# função principal
def game():
    limpa_tela()
    print("\nBem Vindo(a) ao jogo da forca")
    print('-=' * 50)
    print("Descubra o Valor Abaixo!")
    print('-=' * 50)

    # Lista de Palavras 
    palavras = ['carro', 'moto', 'uva', 'peixe', 'humano', 'livros', 'banana', 'macaco', 'escada', 'sol', 'lua', 'refrigerante', 'nave', 'gato', 'cachorro', 'hamster']

    # Escolhendo uma palavra aleatoria
    palavra = random.choice(palavras)
    
    # list comprehension (Retorna '_' para a cada letra da palavra aleatoria)
    letra_descobertas = ['_' for letra in palavra]

    # numero de chances
    chances = 6

    # lista para armazenar letras erradas
    letra_errada = []

    # loop enquanto o valor de chances for maior que 0
    while chances > 0:
        print(' '.join(letra_descobertas))
        print("Chances Restantes:", chances)
        print("Letras Errads:", " ".join(letra_errada))

        # tentativa
        tentativa = input("Digite uma letra: ").lower()

        # Condicional
        if tentativa in palavra:
            index = 0
            for letra in palavra:
                if tentativa == letra:
                    letra_descobertas[index] = letra
                index += 1
        else:
            chances -= 1
            letra_errada.append(tentativa)

            




game()
