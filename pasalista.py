import time
class Estudiantes:
  def __init__(self, nombre, apellido, edad, asistencia="Sin registro"):
    self.nombre = nombre
    self.apellido = apellido
    self.edad = edad
    self.asistencia = asistencia

estudiantes_list = []

while True: 
  time.sleep(1.2)
  print("Bienvenido al gestor de estudiantes \n Por favor, seleccione una opcion:\n")
  print("1. Registrar estudiante")
  print("2. Consultar estudiante")
  print("3. Pasar lista")
  print("4. Salir")
  opcion = int(input("Ingrese una opcion: "))

  if opcion == 1:
    print("Registrar estudiante")
    nombre = input("Ingrese el nombre del estudiante: ")
    apellido = input("Ingrese el apellido del estudiante: ")
    edad = input("Ingrese la edad del estudiante: ")
    estudiante = Estudiantes(nombre, apellido, edad)
    estudiantes_list.append(estudiante)
    print("Estudiante registrado!")
  elif opcion == 2:
    print("Consultar estudiante")
    print("los estudiantes registrados hasta ahora son:\n")
    if estudiantes_list:  
      for estudiante in estudiantes_list:
        print(f"Nombre: {estudiante.nombre}, Apellido: {estudiante.apellido}, Edad: {estudiante.edad},\n Asistencia: {estudiante.asistencia}")
    else:
      print("No hay estudiantes registrados.")
  elif opcion == 3:
    print("Pasar lista")
    if estudiantes_list:  
      for estudiante in estudiantes_list:
        print(f"Estudiante: {estudiante.nombre} {estudiante.apellido}")
        asistencia = input("Asistencia: ")
        estudiante.asistencia = asistencia
  elif opcion == 4:
    time.sleep(1.1)
    print("Saliendo...")
    break 
  else:
    print("Opción inválida. Por favor, ingrese una opción válida.")
