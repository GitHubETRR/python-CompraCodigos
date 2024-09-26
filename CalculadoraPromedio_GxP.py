print('Bienvenido a la calculadora de promedio de goles por partido')
def promedio_goles(goles, partidos):
    if partidos > 0:
        return goles / partidos
    else:
        return 0

partidos = int(input(f"Ingrese el número de partidos jugados: "))
goles = int(input(f"Ingrese el número de goles convertidos: "))

promedio = promedio_goles(goles, partidos)
print(f"Promedio de goles por partido: {promedio}")
