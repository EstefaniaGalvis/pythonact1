# Actividad de la semana 2

nomDueño1 = input("Introduce tu nombre para poder inscribirte en nuestro programa: ")
print (f"Bienvenido, {nomDueño1}")

datoValor1 = input("¿Tienes gatos? (Escribe Sí o No) ")

if datoValor1 == "Sí":
     datoNum1 = int(input("¿Cuantos tienes?" ))
     sumaValores = datoNum1
elif datoValor1 == "No":
    sumaValores = 0
    print("Anotado")

datoValor2 = input("¿Y tienes perros? (Escribe Sí o No) ")

if datoValor2 == "Sí":
    datoNum2 = int(input("¿Cuantos tienes? "))
    if datoValor1 == "Sí":
        sumaValores += datoNum2
    else:
        sumaValores = datoNum2
elif datoValor2 == "No":
    print("Anotado")

if sumaValores > 0:
    print(f"Tienes un total de {sumaValores} mascotas que puedes inscribir en nuestro programa")

nomMascotas = []
for i in range(sumaValores):
    nomMascota = input(f"Ahora ingresa el nombre de tu mascota {i + 1}: ")
    nomMascotas.append(nomMascota)

print("Los nombres de tus mascoticas son: ", nomMascotas)

#Anotaciones para tener ne cuenta en un futuro: Inicializar variables si se debe manejarlas luego!!!!



