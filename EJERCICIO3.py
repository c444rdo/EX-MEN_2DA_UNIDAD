print ("Martínez Estrada Ricardo / NO. de control: 1193 / 31-10-2024")
print (" ")

# Lista de asignaturas
asignaturas = ["Pensamiento Matematico III", "Ecosistemas", "Ciencias Sociales II", "Base de Datos II", "Lengua y Comunicación III"]

# Diccionario para almacenar las notas
notas = {}

# Preguntar al usuario la nota de cada asignatura
for asignatura in asignaturas:
    nota = float(input(f"Ingrese la nota que sacaste en {asignatura}: "))
    notas[asignatura] = nota

# Mostrar las notas obtenidas
for asignatura, nota in notas.items():
    print("En", asignatura, "has sacado", nota, ".")