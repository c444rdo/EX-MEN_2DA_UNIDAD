print ("Martínez Estrada Ricardo / NO. de control: 1193 / 31-10-2024")
print (" ")

# Diccionario con los créditos de las asignaturas
asignaturas_creditos = {'Pensamiento Matemático III': 10, 'Lengua y Comunicación III': 6, 'Ecosistemas': 7}

# Variable para almacenar el total de créditos
total_creditos = 0

# Mostrar los créditos de cada asignatura
for asignatura, creditos in asignaturas_creditos.items():
    print(asignatura, "tiene", creditos, "créditos.")
    total_creditos += creditos

# Mostrar el total de créditos del curso
print("El número total de créditos del curso es: ", total_creditos)