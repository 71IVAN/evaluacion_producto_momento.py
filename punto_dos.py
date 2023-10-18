# Crea un diccionario vacío llamado Departamentos
# Ingresa el nombre del Departamento como llave y su Capital como valor.
# Crea ciclo para imprimir el Departamento y la capital
# • Escoge un departamento al azar (random)
# • Solicita al usuario que ingrese su capital
# • Si la capital es incorrecta debe seguir solicitando la capital hasta que se ingrese la correcta.
# • Si el usuario escribe salir, el programa termina. (crear Menú)
# • Si el usuario escribe la capital correcta, imprima Correcto.
# • Tiene tres intentos por departamento. Si el usuario no acierta debe imprimir “Hasta luego”, sigue
# intentando en otra oportunidad.

import random

departamentos = {
    'Amazonas': 'Leticia', 
    'Antioquia': 'Medellin', 
    'Arauca': 'Arauca', 
    'Atlantico': 'Barranquilla', 
    'Caldas': 'Manizales'
    }

while True:
    print("------ Adivina la capital ------")
    print("\n")
    print("Debes adivinar la capital del departamento.")
    print("Tienes 3 intentos, si quieres salir en cualquier momento, escribe 'salir'.")
    print("Para jugar, escribe 'go' o '1'.")
    print("\n")

    option = input("¿Qué quieres hacer?  ")

    if option == '1' or option.lower() == 'go':
        oportunidades = 0
        while oportunidades < 3:
            departamento_aleatorio = random.choice(list(departamentos.keys()))
            adivina = input(f"Cual es la capital de {departamento_aleatorio} : ").capitalize()

            if adivina == departamentos[departamento_aleatorio]:
                print(f"¡Correcto! La capital es {departamentos[departamento_aleatorio]}")
                break
            elif adivina == 'Salir':
                break
            elif adivina.isdigit():
                print("Error, no se admiten números")
            else:
                print("Capital incorrecta")

            oportunidades += 1

        if oportunidades == 3:
            print("Has agotado tus 3 intentos. La capital correcta es:", departamentos[departamento_aleatorio])

    elif option.lower() == 'salir':
        print("Hasta luego, has decidido salir del juego.")
        break

    else:
        print("Opción inválida. Por favor, elige 'go', '1' o 'salir'.")

