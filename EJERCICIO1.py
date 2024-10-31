print ("Martínez Estrada Ricardo / NO. de control: 1193 / 31-10-2024")
print (" ")

# Lista de asignaturas
asignaturas = ["Pensamiento Matemático III", "Ecosistemas", "Humanidades III", "Inglés III", "Lengua y Comunicación III"]

# Preguntar al usuario la nota de cada asignatura
for asignatura in asignaturas[:]:  # Usamos una copia para evitar problemas al eliminar elementos
    nota = float(input(f"Ingresa tu calificación en {asignatura}: "))
    
    # Suponiendo que la nota de aprobación es 6.0
    if nota >= 6.0:
        asignaturas.remove(asignatura)

# Mostrar las asignaturas que el usuario tiene que repetir
if asignaturas:
    print("Tienes que repetir las siguientes materias (por burro):")
    for asignatura in asignaturas:
        print(asignatura)
else:
    print("¡Felicidades! Pasaste todas las materias.")