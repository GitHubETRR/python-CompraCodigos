print('Bienvenido a la calculadora de promedio de goles por partido')
opcion=int(input("1. Delantero \n 2. Arquero \n"))

def promedio_goles(goles, partidos):
    if partidos > 0:
        return goles / partidos
    else:
        return 0
        
def promedio_atajadas(atajadas, partidos):
    if partidos > 0:
        return atajadas / partidos
    else:
        return 0

if opcion==1:
    partidos = int(input(f"Ingrese el número de partidos jugados: "))
    goles = int(input(f"Ingrese el número de goles convertidos: "))
    
    promedioG = promedio_goles(goles, partidos)
    print(f"Promedio de goles por partido: {promedioG}")

elif opcion==2:
    partidos = int(input(f"Ingrese el número de partidos jugados: "))
    atajadas = int(input(f"Ingrese el número de atajadas: "))
    
    promedioA = promedio_atajadas(atajadas, partidos)
    print(f"Promedio de atajadas por partido: {promedioA}")