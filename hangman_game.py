from words import palabras

import random 

def obtener_palabra_válida(párametropalabras):
    #Select a word at random.
    palabra = random.choice(palabras)

    #while '-' in palabra or ' ' in palabra: pala


def ahorcado():

    print("==========================")
    print("Bienvenido(a) al juego del ahorcado")
    print("==========================")

    palabra = obtener_palabra_válida(palabras)