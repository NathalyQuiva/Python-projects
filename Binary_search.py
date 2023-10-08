import random
import time #To measure the total time in every search


def búsqueda_ingenua(lista, objetivo):
    for i in range(len(lista)):
        if lista[i] == objetivo:
            return i
    return -1


def búsqueda_binaria(lista, objetivo, límite_inferior=None, límite_superior=None):

    if límite_inferior is None:
        límite_inferior = 0
    if límite_superior is None: 
        límite_superior = len(lista)-1
    if límite_superior < límite_inferior:
        return -1
    
    punto_medio = (límite_inferior +  límite_superior)//2#//This take only the integer

    if lista[punto_medio] == objetivo:
        return punto_medio
    elif objetivo < punto_medio:
        return búsqueda_binaria(lista, objetivo, límite_inferior, límite_superior = punto_medio-1)
    else: 
        return búsqueda_binaria(lista, objetivo, punto_medio + 1, límite_superior)


if __name__ =='__main__':
    lista = [1,3,5,10,12]
    print(búsqueda_binaria(lista, 10))
# lista = [1,3,5,10,12]
# print(búsqueda_ingenua(lista, 17))
    tamaño = 1000
    conjunto_inicial = set()

    while len(conjunto_inicial) < tamaño:
        conjunto_inicial.add(random.randint(-3*tamaño,3*tamaño))

    lista_ordenada = sorted(list(conjunto_inicial))

    inicio = time.time()
    for objetivo in lista_ordenada :
        búsqueda_ingenua(lista_ordenada,objetivo)
        fin = time.time()
        print(f"Tiempo de busqueda ingenua: {fin-inicio} segundos.")

    inicio = time.time()
    for objetivo in lista_ordenada:
        búsqueda_binaria(lista_ordenada, objetivo)
        fin = time.time()
        print(f"Tiempo de búsqueda binaria: {fin - inicio} segundos.")

#try to decrease the complexity 