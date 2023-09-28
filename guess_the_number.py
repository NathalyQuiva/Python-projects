#Interactive game, in this game the computer generates a number and the user tries to guess the number. 
import random 


def adivina_el_número(x):

    print("===========================")
    print("Bienvenido(a) al Juego!")
    print("===========================")
    print("Tu meta es adivinar el número generado por la computadora.")

    número_aleatorio = random.randint(1,x)

    predicción = 0

    while predicción !=número_aleatorio:
        predicción = int(input(f"Adivina un número  entre 1 y {x}: "))

        if predicción < número_aleatorio:
            print("Intenta otra vez.Este número es muy pequeño.")
        if predicción > número_aleatorio:
            print("Intenta otra vez.Este número es muy grande.")
        
    print(f"¡Felicitaciones! Adivinaste el número")


adivina_el_número(10)
    #This is a python function, this must have two point in the end.  
#x=limite superior
#Next, the funcionality of the game is developed.


