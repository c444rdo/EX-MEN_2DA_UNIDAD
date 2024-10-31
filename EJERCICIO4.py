print ("Martínez Estrada Ricardo / NO. de control: 1193 / 31-10-2024")
print (" ")

# Preguntar al usuario por su información
nombre = input("¿Cuál es tu nombre? ")
edad = input("¿Cuál es tu edad? ")
direccion = input("¿Cuál es tu dirección? ")
telefono = input("¿Cuál es tu número de teléfono? ")

# Almacenar la información en un diccionario
usuario = {
    'nombre': nombre,
    'edad': edad,
    'direccion': direccion,
    'telefono': telefono
}

# Mostrar la información del usuario
print (usuario['nombre'], "tiene", usuario['edad'], "años, vive en", usuario['direccion'], "y su número de teléfono es", usuario['telefono'])
