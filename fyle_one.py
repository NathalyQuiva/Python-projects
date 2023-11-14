import file_two

print("File one __name__ is set to: {}". format(__name__))

if __name__ == "__main__":
    print("File one executed when ran directly")
else:
    print("File one executed when imported")

#la variable __name__ es __main__ para el archivo que se ejecuta y para todos los demás que son importados será el nombre del módulo.