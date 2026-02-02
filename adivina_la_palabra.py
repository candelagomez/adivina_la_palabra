import random

palabras = [
        "codigo", "programa", "software", "aplicacion", "sistema",
        "datos", "modelo", "algoritmo", "logica", "proceso",
        "funcion", "variable", "resultado", "entrada", "salida",
        "aprendizaje", "entrenamiento", "prediccion", "analisis", "decision",
        "automatizacion", "inteligencia", "artificial", "lenguaje", "texto",
        "imagen", "voz", "respuesta", "asistente", "chat",
        "error", "prueba", "mejora", "control", "flujo",
        "red", "conexion", "archivo", "memoria",
        "evaluacion", "patron", "ejemplo", "simulacion",
        "interaccion", "usuario"
]

palabra_secreta = random.choice(palabras)
vidas = 7
palabras_incorrectas = []
tablero = []

for letra in palabra_secreta:
    tablero.append("_")

while vidas > 0:
    print(f"Vidas: {vidas}")
    print(tablero)
    letra_ingresada = input("Ingresa una letra: ").lower()
    if letra_ingresada.isalpha():

        if letra_ingresada in palabra_secreta:
            print("¡Adivinaste una letra!")

            for i in range(len(palabra_secreta)):
                if palabra_secreta[i] == letra_ingresada:
                    tablero[i] = letra_ingresada
            if "_" not in tablero:
                print(f"Ganaste, la palabra era: {palabra_secreta}!")
                print(tablero) 
                vidas = 0 
        else:
            print("Incorrecto, esa letra no está")
            vidas = vidas - 1

    else:
        print("Error: Por favor ingresa solo letras.")
        
if "_" in tablero:
    print(f"¡Perdiste! Te quedaste sin vidas. La palabra era: {palabra_secreta}")