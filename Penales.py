import random
LadoArquero = 0

print("Bienvenido al simulador de penales. ")
print("Por favor, decida a donde patear \n")
print(" 1. Arriba a la derecha \n 2. Arriba a la izquierda \n 3. Abajo a la derecha \n 4. Abajo a la izquierda \n 5. Fuerte al medio \n")
print(" o__        o__     |   |\ ")
print("/|          /\      |   |X\ ")
print("/ > o        <\     |   |XX\ ")
print("\n")

LadoPatear = int(input("¡¡Decidí a donde patear pibe de oro!!"))
LadoArquero = random.randint(1,5)


if LadoArquero!=LadoPatear:
    print("...La proxima será")
    
else: 
    print("¡¡¡Dale Campeooon Dale campeooon!!!")
    
    print("         ____ ")
    print("        ( () ) ")
    print("         \  / ")
    print("          || ")
    print("          || ")
    print("         [__] ")
    print("        /)  (\ ")
    print("       (( () )) ")
    print("         \__// ")
    print("         `..' ")
    print("          || ")
    print("          || ")
    print("         // \__ ")
    print("      _ ((  `--' ")
    print("     (_) \) ")
    print("---------------------- ")



