import random
import time #To measure the total time in every search


def búsqueda_ingenua(lista, objetivo):
    for i in range(len(lista)):
        if lista[i] == objetivo:
            return i
    return -1


def búsqueda_binaria(lista, objetivo, límite_inferior=None, límite_superior=None):
# The list must be ordered in ascending way
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
        return búsqueda_binaria(lista, objetivo, límite_inferior, límite_superior = punto_medio)


# lista = [1,3,5,10,12]
# print(búsqueda_ingenua(lista, 17))
