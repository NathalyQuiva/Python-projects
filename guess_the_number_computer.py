import random 


def adivina_el_número_computadora(x):

    print("==========================")
    print("Bienvenido(a) al juego")
    print("=========================")
    print(f"Selecciona un número entre 1 y {x} para que la computadora intente adivinarlo")

    límite_inferior = 1
    límite_superior = x

    respuesta = ""
    while respuesta != "c":
        # Generar prediccion 
        if límite_inferior != límite_superior:
            predicción  = random. randint(límite_inferior, límite_superior)
        else: 
            predicción = límite_inferior

        respuesta = input(f"Mi predicción es {predicción}. Si es muy alta, ingresa (A). Si es muy baja, ingresa (B). Si es correcto ingresa (C): ").lower()

        if respuesta == "a":
            límite_superior = predicción - 1
        elif respuesta == "b":
            límite_superior = predicción + 1 

    print(f"¡Siii! La computadora adivinó tu número correctamente: {predicción}")


adivina_el_número_computadora(10)

##Main Branch with only 3 games