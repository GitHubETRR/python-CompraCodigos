print ("Bienvenido al programón de Facundo Vasile")
print("Por favor, ingrese una fecha de nacimiento")
Dia = int (input("Ingrese el dia (En formato numerico)"))
Mes = int (input("Ingrese el mes (En formato numerico)"))
Año = int (input("Ingrese el año (En formato numerico)"))

def obetener_nombre_mes(Mes):
    meses = {
        1: "Enero",
        2: "Febrero",
        3: "Marzo",
        4: "Abril",
        5: "Mayo",
        6: "Junio",
        7: "Julio",
        8: "Agosto",
        9: "Septiembre",
        10: "Octubre",
        11: "Noviembre",
        12: "Diciembre",
    }
    return meses[Mes]

print (f"La persona nació el {Dia} de {obetener_nombre_mes(Mes)} del {Año}" )