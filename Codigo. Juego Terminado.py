# PROYECTO INTEGRADOR
# Juego: Adivina el Número

# USAMOS LA FUNCIÓN: Mostrar la bienvenida al usuario y las instrucciones

def mostrar_bienvenida():
    print("------------------------------------------")
    print("        JUEGO ADIVINA EL NÚMERO")
    print("------------------------------------------")
    print("Piensa en un número entre 1 y 100.")
    print("Yo intentaré adivinarlo.")
    input("\nCuando estés listo presiona ENTER...")



# FUNCIÓN: Obtener una respuesta válida, en la que solo acepta: mayor, menor o correro

def pedir_respuesta():

    while True:

        respuesta = input(
            "\n¿El número es mayor, menor o correcto?: "
        ).lower().strip()

        if respuesta in ["mayor", "menor", "correcto"]:
            return respuesta

        print("Respuesta inválida.")
        print("Escribe únicamente:")
        print("mayor")
        print("menor")
        print("correcto")

# FUNCIÓN PRINCIPAL DEL JUEGO

def jugar():

    # Límites iniciales
    minimo = 1
    maximo = 100

    # Contador de intentos
    intentos = 0

    # Bucle principal
    while True:

        # Calcula el número del medio
        intento = (minimo + maximo) // 2

        # Cuenta un intento
        intentos += 1

        # Muestra el número propuesto
        print(f"\nIntento #{intentos}")
        print(f"¿Es {intento}?")

        # Solicita la respuesta del usuario
        respuesta = pedir_respuesta()

        # Si acertó termina el juego
        if respuesta == "correcto":

            print("\n------------------------------------")
            print("¡¡He adivinado tu número!!")
            print(f"Número encontrado: {intento}")
            print(f"Intentos realizados: {intentos}")
            print("Gracias por jugar.")
            print("--------------------------------------")

            break

        # Si el número es mayor
        elif respuesta == "mayor":
            minimo = intento + 1

        # Si el número es menor
        elif respuesta == "menor":
            maximo = intento - 1

        # Verifica respuestas contradictorias
        if minimo > maximo:
            print("\nLas respuestas ingresadas son contradictorias.")
            print("El juego finalizará.")
            break



# PROGRAMA PRINCIPAL


mostrar_bienvenida()

jugar()

input("\nPresiona ENTER para salir...")
