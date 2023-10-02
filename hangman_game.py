from words import palabras
import string
from ahorcado_diagramas import vidas_diccionario_visual


import random 

def obtener_palabra_válida(párametropalabras):
    #Select a word at random.
    palabra = random.choice(palabras)

    while '-' in palabra or ' ' in palabra: 
        palabra = random.choice(palabras)

    return palabra.upper()


def ahorcado():

    print("==========================")
    print("Bienvenido(a) al juego del ahorcado")
    print("==========================")
    

    palabra = obtener_palabra_válida(palabras)

    letras_por_adivinar = set(palabra)
    letras_adivinadas = set()
    abecedario = set(string.ascii_uppercase)

    vidas = 7

    while len(letras_por_adivinar) > 0 and vidas > 0:
        print(f"Te quedan {vidas} vidas y haz usado estas letras: {'  '.join(letras_adivinadas)}")
        #To Show th word's real state , list comprehension:
        palabra_lista= [letra if letra in letras_adivinadas else '-' for letra in palabra]
        print(vidas_diccionario_visual[vidas])
        #To shown the letras with space between these
        print(f"Palabra: {' '.join(palabra_lista)}")

        letra_usuario = input("Escoge una letra: ").upper()

        if letra_usuario in abecedario - letras_adivinadas:
            letras_adivinadas.add(letra_usuario)

            if letra_usuario in letras_por_adivinar:
                letras_por_adivinar.remove(letra_usuario)
                print('')
            else:
                vidas -= 1
                print(f"\n Tu letra {letra_usuario} no está en la palabra.")
        # If the word choose for the user was in the gueses words
        elif letra_usuario in letras_adivinadas:
            print("\n Ya escogiste esa letra.Por favor escoge una letra nueva")
        else:
            print("\n Esta letra no es válida")


# Pregunta de la aplicacion de Python:
# 
# def transform(a = 2):
#     if a == 1:
#         return a +- 2
#     return a

# total = 1

# for x in [3,5,1]:
#     total = total + transform(x)

# print(total)