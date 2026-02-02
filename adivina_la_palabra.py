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
