class Liga:
  tipo = 'futbol'
  año = 2024
  def __init__(self, nombre, equipos):
    self.nombre = nombre
    self.equipos = equipos

premier = Liga('Premier League', ["Arsenal","Tottenham","Man. United", "Man. City", "Liverpool", "Chelsea", "West Ham", "Wolves", "Leicester", "Aston Villa", "Newcastle", "Brighton", "Brentford", "Fulham", "Crystal Palace", "Southampton", "Everton", "Bournemouth", "Nottingham Forest", "Ipswich"])

Laliga = Liga('La Liga', ["Real Madrid", "Barcelona", "Atletico Madrid" , "Sevilla", "Valencia", "Real Betis", "Athletic Bilbao", "Villarreal", "Real Sociedad", "Celta Vigo", "Alavés", "Girona", "Osasuna", "Getafe", "Leganés", "Real Valladolid","Real Mallorca", "Espanyol", "Valencia", "Rayo Vallecano"])

SerieA = Liga('Serie A', ["Juventus", "Inter Milan", "Napoli", "Roma", "Lazio", "Milan", "Atalanta", "Venezia", "Torino", "Empoli", "Fiorentina", "Parma", "Monza", "Lecce", "Udinese", "Bologna", "Cagliari", "Spezia", "Verona", "Como"])

Bundesliga = Liga('Bundesliga', ["Bayern Munchen" , "Borussia Dortmund", "RB Leipzig", "Eintracht Frankfurt", "VfB Stuttgart", "Werder Bremen", "Hoffenheim", "Borussia M'gladbach", "Union Berlin", "1. FC Koeln", "SC Freiburg", "FC Augsburg","Holstein Kiel","St. Pauli","Mainz 05","Bochum","Heidenheim","Wolfsburg"])

LPFA = Liga('LPFA' ,["Boca Juniors", "RiBer Plate", "Independiente", "Racing", "San Lorenzo", "Defensa y Justicia", "Platense", "Estudiantes","Huracan","Talleres","Belgrano","Rosario central","Tigre","Gimnasia y esgrima de la plata","Independiente Rivadavia","Sarmiento","Lanus","Banfield","Instituto","Godoycruz","Riestra","Atletico","Union","Velez","Newells","Barracas central", "Central Cordoba","Argentinos juniors"])

Ligue1 = Liga('Ligue 1', ["PSG", "Monaco", "Marsella", "Lyon", "Nice", "Lille", "Rennes", "Montpellier","Nantes", "Toulouse", "Strasbourg", "Angers","Saint-Etienne", "Auxerre", "Le Havre" , "Lens", "Reims", "Stade Brestois 29"])

Eredivisie = Liga( 'Eredivisie', ["Ajax", "Feyenoord", "PSV", "AZ", "Heerenveen","FC Utrecht", "FC Groningen", "FC Twente", "Willem II" , "F. Sittard", "NEC", "FC Vitesse", "FC Heracles","RKC Waalwijk","PEC Zwolle","Go ahead","Almere city","NAC Breda"])

PrimeraDivParaguay = Liga('Primera División Paraguay', ["Olimpia", "Cerro Porteño", "2 De Mayo", "Nacional", "Libertad", "General Caballero", "Guaraní", "Sportivo Trinidense", "Sportivo Luqueño", "Sportivo Ameliano", "Tacuary", "Sol De America"])

ligas = [premier, Laliga,Ligue1,Eredivisie,Bundesliga, SerieA, LPFA, PrimeraDivParaguay]
print("Bienvenido, por favor seleccione una liga de futbol")
opcion = int(input(" 1. Premier League \n 2. La liga \n 3. Ligue 1 \n 4. Eredivisie \n 5. Bundesliga \n 6. Serie A \n 7. LPFA\n 8. Primera Division Paraguay\n"))
print("Los equipos son:")
if opcion in range(1,9):
    lista_de_equipos = ligas[opcion-1].equipos
    for equipo in lista_de_equipos:
      print(equipo)
else:
    print("Opción incorrecta.")

"""
if opcion == '1':
  lista_de_equipos = ligas[int(opcion)-1].equipos
  for equipo in lista_de_equipos:
    print(equipo)
elif opcion == '2':
  lista_de_equipos = ligas[int(opcion)-1].equipos
  for equipo in lista_de_equipos:
    print(equipo)
elif opcion == '3':
  lista_de_equipos = ligas[int(opcion)-1].equipos
  for equipo in lista_de_equipos:
    print(equipo)
elif opcion == '4':
  lista_de_equipos = ligas[int(opcion)-1].equipos
  for equipo in lista_de_equipos:
    print(equipo)
elif opcion == '5':
  lista_de_equipos = ligas[int(opcion)-1].equipos
  for equipo in lista_de_equipos:
    print(equipo)
elif opcion == '6':
  lista_de_equipos = ligas[int(opcion)-1].equipos
  for equipo in lista_de_equipos:
    print(equipo)
elif opcion == '7':
  lista_de_equipos = ligas[int(opcion)-1].equipos
  for equipo in lista_de_equipos:
    print(equipo)
"""
