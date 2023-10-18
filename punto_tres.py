#Agregandole funciones al punto Dos.
import random

departamentos = {
    'Amazonas': 'Leticia',
    'Antioquia': 'Medellín',
    'Arauca': 'Arauca',
    'Atlantico': 'Barranquilla',
    'Caldas': 'Manizales'
}

def adivina_capital(departamentos):
    departamento, capital = random.choice(list(departamentos.items()))
    return departamento, capital

def menu():
    print("------ Adivina la capital ------\n")
    print("Debes adivinar la capital del departamento.")
    print("Tienes 3 intentos, sino quieres jugar escribe 'salir'.")
    print("Para jugar, escribe 'go' o '1'.\n")

    oportunidades = 0
    es_numero = lambda s: s.isnumeric()

    while True:
        option = input("¿Qué quieres hacer?  ")

        if option == '1' or option == 'go':
            departamento, capital = adivina_capital(departamentos)

            while oportunidades < 3:
                adivina = input(f"Cual es la capital de {departamento} : ").capitalize()

                if adivina == capital:
                    print(f"¡Correcto! La capital es {capital}")
                    break
                elif adivina == 'Salir':
                    break
                elif es_numero(adivina):
                    print("Error, no se admiten números")
                else:
                    print("Capital incorrecta")

                oportunidades += 1

            if oportunidades == 3:
                print(f"Has agotado tus 3 intentos. La capital correcta es: {capital}")

        elif option.lower() == 'salir':
            print("Hasta luego, has decidido salir del juego.")
            break

        else:
            print("Opción inválida. Por favor, elige 'go', '1' o 'salir'.")

if __name__ == "__main__":
    menu()