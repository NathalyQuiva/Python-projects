import random 


def jugar():
    usuario = input("Escoge una opción: 'pi' para piedra, 'pa' para papel o 'ti' para tijera.\n").lower()
    computadora = random.choice(['pi', 'pa', 'ti'])
                                
    if usuario == computadora:
        print(f"Soy la computadoraaa Buaaajajaja y escojo : {computadora}")
        return '¡Empate!'       

    if ganó_el_jugador(usuario, computadora): 
        print(f"Soy la computadoraaa Buaaajajaja y escojo : {computadora}")
        return '¡Ganaste!'
    
    else:
        print(f"Soy la computadoraaa Buaaajajaja y escojo : {computadora}")
        return '¡Perdiste!'                  


def ganó_el_jugador(jugador, oponente):
    if((jugador == 'pi' and oponente == 'ti')
       or (jugador == 'pa' and oponente == 'pi')
       or (jugador == 'ti' and oponente == 'pa')): 
       return True
    else:
        return False 
    
print(jugar())



#Return True if win the player.
#Rock beats scissors (rock>sci)
#Scissors beats paper (sci>pa)
#Paper beats rock (pa>pi)
   
