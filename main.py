print("Juego Adivina el número iniciado")

# PASO 1: instrucciones claras al usuario
print("Piensa un número entre 1 y 100.")
input("Cuando estés listo presiona ENTER...")

# PASO 2: límites iniciales
min_val = 1
max_val = 100

# PASO 3: inicio del juego
while True:
    intento = (min_val + max_val) // 2
    print("¿Es", intento, "?")

    respuesta = input("mayor / menor / correcto: ").lower()

    if respuesta == "correcto":
        print("Adivine el numero, GRACIAS POR JUGAR")
        break
    elif respuesta == "mayor":
        min_val = intento + 1
    elif respuesta == "menor":
        max_val = intento - 1
        
        