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

